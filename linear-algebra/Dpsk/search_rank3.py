"""Deterministic search for a 4x4 integer matrix A with
  1. rank(A) == 3 exactly
  2. integer RREF R (denominators 1, well within <= 3)
  3. integer nullspace n (last entry normalised to 1), |n_i| <= 8
  4. no zero row, not block-triangular / trivially decomposable
  5. entries in -4..4, all 16 nonzero, mixed signs (exam-like)
  +  pivots in columns 0,1,2
  +  top-left 3x3 block P unimodular (det = +-1) with small inverse,
     which yields a clean integer particular-solution formula.

Standard library only; all linear algebra exact via fractions.Fraction.
"""
import random
from fractions import Fraction
from functools import reduce
from math import gcd
from itertools import combinations


# ---------------- exact linear algebra ----------------

def rref(M):
    R = [[Fraction(x) for x in row] for row in M]
    rows, cols = len(R), len(R[0])
    pivots = []
    r = 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if R[i][c] != 0), None)
        if p is None:
            continue
        R[r], R[p] = R[p], R[r]
        pv = R[r][c]
        R[r] = [x / pv for x in R[r]]
        for i in range(rows):
            if i != r and R[i][c] != 0:
                f = R[i][c]
                R[i] = [a - f * b for a, b in zip(R[i], R[r])]
        pivots.append(c)
        r += 1
        if r == rows:
            break
    return R, pivots


def rank(M):
    return len(rref(M)[1])


def nullspace(M):
    R, pivots = rref(M)
    cols = len(M[0])
    basis = []
    for fc in [c for c in range(cols) if c not in pivots]:
        v = [Fraction(0)] * cols
        v[fc] = Fraction(1)
        for i, pc in enumerate(pivots):
            v[pc] = -R[i][fc]
        basis.append(v)
    return basis


def left_nullspace(M):
    Mt = [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]
    return nullspace(Mt)


def matvec(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]


def vec_mat(v, M):
    return [sum(v[i] * M[i][j] for i in range(len(M))) for j in range(len(M[0]))]


def det3(P):
    return (P[0][0] * (P[1][1] * P[2][2] - P[1][2] * P[2][1])
            - P[0][1] * (P[1][0] * P[2][2] - P[1][2] * P[2][0])
            + P[0][2] * (P[1][0] * P[2][1] - P[1][1] * P[2][0]))


def inv3(P):
    """Exact inverse: inv[i][j] = (-1)^(i+j) * M_ji / det(P),
    where M_ji is the minor obtained by deleting row j and column i."""
    d = det3(P)
    if d == 0:
        return None
    inv = [[None] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            minor = [[P[a][b] for b in range(3) if b != i]
                     for a in range(3) if a != j]
            cof = minor[0][0] * minor[1][1] - minor[0][1] * minor[1][0]
            inv[i][j] = Fraction((-1) ** (i + j) * cof, d)
    return inv


def integerise(v):
    """Scale a Fraction vector to primitive integer vector with first
    nonzero entry positive."""
    den = reduce(lambda a, b: a * b // gcd(a, b), [x.denominator for x in v], 1)
    iv = [int(x * den) for x in v]
    g = reduce(gcd, [abs(x) for x in iv if x != 0], 0)
    if g > 1:
        iv = [x // g for x in iv]
    if next(x for x in iv if x != 0) < 0:
        iv = [-x for x in iv]
    return iv


# ---------------- structural filters ----------------

def has_zero_row(M):
    return any(all(x == 0 for x in row) for row in M)


def is_block_triangular(M):
    """True if some nonempty proper index subset S is closed: rows in S touch
    only columns in S, or columns in S are touched only by rows in S
    (block upper/lower triangular after a permutation)."""
    n = len(M)
    for k in range(1, n):
        for S in combinations(range(n), k):
            Sset = set(S)
            out = [j for j in range(n) if j not in Sset]
            if all(M[i][j] == 0 for i in S for j in out):
                return True
            if all(M[j][i] == 0 for i in S for j in out):
                return True
    return False


def exam_like(M):
    vals = [x for row in M for x in row]
    if any(v == 0 for v in vals):            # dense: kills sparse/block look
        return False
    if all(v > 0 for v in vals) or all(v < 0 for v in vals):
        return False
    pos = sum(1 for v in vals if v > 0)
    neg = sum(1 for v in vals if v < 0)
    if min(pos, neg) < 4:
        return False
    return len(set(vals)) >= 6


def no_obvious_dependency(M):
    """Reject matrices whose rank-3 nature is instantly visible:
    two proportional rows, two proportional columns, or one row equal to
    +-(row_j + row_k) / +-(row_j - row_k)."""
    def check(R):
        n = len(R)
        for i, j in combinations(range(n), 2):
            if all(R[i][k] * R[j][0] == R[j][k] * R[i][0] for k in range(n)):
                return False                      # proportional rows
        for i in range(n):
            others = [x for x in range(n) if x != i]
            for j, k in combinations(others, 2):
                for s1 in (1, -1):
                    for s2 in (1, -1):
                        if all(R[i][t] == s1 * R[j][t] + s2 * R[k][t]
                               for t in range(n)):
                            return False
        return True

    Mt = [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]
    return check(M) and check(Mt)


# ---------------- search ----------------

def search(limit=5000000, seed=12345, require_unimodular=True,
           max_inv_entry=4, verbose_every=100000):
    random.seed(seed)
    trials = 0
    while trials < limit:
        trials += 1
        if verbose_every and trials % verbose_every == 0:
            print("  ... trials =", trials, flush=True)
        M = [[random.randint(-4, 4) for _ in range(4)] for _ in range(4)]
        if not exam_like(M):
            continue
        if not no_obvious_dependency(M):
            continue
        if has_zero_row(M) or is_block_triangular(M):
            continue
        if rank(M) != 3:
            continue
        R, pivots = rref(M)
        if pivots != [0, 1, 2]:
            continue
        if any(x.denominator != 1 for row in R for x in row):
            continue
        n = nullspace(M)[0]
        if n[3] == 0:
            continue
        n = [x / n[3] for x in n]
        if any(x.denominator != 1 for x in n):
            continue
        ni = [int(x) for x in n]
        if any(abs(x) > 8 for x in ni):
            continue
        if any(x == 0 for x in ni):          # every column genuinely participates
            continue
        P = [row[:3] for row in M[:3]]
        d = det3(P)
        if d == 0:
            continue
        if require_unimodular:
            if abs(d) != 1:
                continue
            Pi = inv3(P)
            if any(x.denominator != 1 for row in Pi for x in row):
                continue
            if max(abs(x) for row in Pi for x in row) > max_inv_entry:
                continue
        return M, R, pivots, ni, trials
    return None


# ---------------- reporting ----------------

def main():
    print("=== SEARCH: dense, all 16 entries nonzero, mixed signs, entries -4..4,")
    print("    rank 3, integer RREF, pivots 0,1,2, |n_i|<=8, unimodular top-left 3x3 ===")
    res = search()
    relaxations = []
    if res is None:
        relaxations.append("unimodular top-left 3x3 requirement dropped")
        print("relaxing:", relaxations[-1])
        res = search(require_unimodular=False)
    if res is None:
        print("NO MATRIX FOUND")
        return
    M, R, pivots, ni, trials = res
    print("trials =", trials)
    print("relaxations =", relaxations if relaxations else "none - all constraints met")
    print()

    ok_all = True

    def chk(label, cond):
        nonlocal ok_all
        ok_all = ok_all and bool(cond)
        print(f"[{'PASS' if cond else 'FAIL'}] {label}")

    print("=== MATRIX ===")
    print("A =", M)
    print("nonzero entries:", sum(1 for r in M for x in r if x != 0), "/ 16",
          "| positive:", sum(1 for r in M for x in r if x > 0),
          "| negative:", sum(1 for r in M for x in r if x < 0),
          "| distinct values:", len({x for r in M for x in r}))
    print()

    print("=== VERIFICATION 1: rank and RREF ===")
    rk = rank(M)
    print("exact rank(A) =", rk)
    chk("rank(A) == 3 exactly", rk == 3)
    print("RREF R (exact Fractions):")
    for row in R:
        print("   ", [str(x) for x in row])
    print("R as integers:", [[int(x) for x in row] for row in R])
    chk("RREF R has all integer entries (denominator 1 <= 3)",
        all(x.denominator == 1 for row in R for x in row))
    chk("R has exactly 3 pivot columns", len(pivots) == 3)
    chk("R has exactly one all-zero row",
        sum(1 for row in R if all(x == 0 for x in row)) == 1)
    chk("pivot columns == [0,1,2]", pivots == [0, 1, 2])
    chk("R is genuinely the RREF of A (recomputed)",
        rref(M)[0] == R and rref(M)[1] == pivots)
    print("pivot columns:", pivots)
    print()

    print("=== VERIFICATION 2: nullspace ===")
    ns = nullspace(M)
    print("dim nullspace =", len(ns))
    chk("nullspace is 1-dimensional", len(ns) == 1)
    print("nullspace n (integer, last entry 1) =", ni)
    An = matvec(M, [Fraction(x) for x in ni])
    print("A @ n =", [str(x) for x in An])
    chk("A @ n == 0 exactly", all(x == 0 for x in An))
    chk("all |n_i| <= 8", all(abs(x) <= 8 for x in ni))
    chk("n == (-f, 1) with f = R[:,3]", ni == [-int(R[i][3]) for i in range(3)] + [1])
    print()

    print("=== VERIFICATION 3: no zero row / not block-triangular ===")
    chk("A has no all-zero row", not has_zero_row(M))
    chk("A is not block-triangular (no closed proper subset of indices)",
        not is_block_triangular(M))
    chk("no two rows / two columns are proportional, and no row is "
        "+-(row_j +- row_k)  [rank deficiency is not instantly visible]",
        no_obvious_dependency(M))
    print()

    print("=== VERIFICATION 4: consistency condition y^T b = 0 ===")
    yns = left_nullspace(M)
    print("dim left nullspace =", len(yns))
    chk("left nullspace is 1-dimensional", len(yns) == 1)
    y = integerise(yns[0])
    print("y (integer, primitive) =", y)
    yA = vec_mat([Fraction(x) for x in y], M)
    print("y^T A =", [str(x) for x in yA])
    chk("y^T A == 0 exactly", all(x == 0 for x in yA))
    chk("all |y_i| small (<= 60)", all(abs(x) <= 60 for x in y))
    print()

    print("=== VERIFICATION 5: particular solution ===")
    P = [row[:3] for row in M[:3]]
    Pi = inv3(P)
    print("B = first 3 columns of A; P = top-left 3x3 block of A =", P)
    print("det(P) =", det3(P))
    print("P^-1 (integer matrix) =",
          [[str(x) for x in row] for row in Pi])
    chk("P is unimodular, so P^-1 is an integer matrix",
        det3(P) in (1, -1) and all(x.denominator == 1 for row in Pi for x in row))
    prod = [[sum(Fraction(P[i][k]) * Pi[k][j] for k in range(3)) for j in range(3)]
            for i in range(3)]
    chk("P @ P^-1 == I exactly (inverse is correct, not transposed)",
        prod == [[Fraction(1 if i == j else 0) for j in range(3)] for i in range(3)])
    print()
    print("Claimed formula (from the task):  xp = (b1,b2,b3,0)")
    print("Correct formula:                  xp = (P^-1 @ (b1,b2,b3)^T, 0)")

    def consistent(b):
        return sum(Fraction(y[i]) * b[i] for i in range(4)) == 0

    # build 4 consistent integer b
    tests = []
    random.seed(999)
    while len(tests) < 4:
        cand = [random.randint(-9, 9) for _ in range(4)]
        if y[3] != 0:
            s = sum(y[i] * cand[i] for i in range(3))
            if s % y[3] != 0:
                continue
            cand[3] = -s // y[3]
        else:
            if y[2] == 0:
                continue
            s = sum(y[i] * cand[i] for i in range(2)) + y[3] * cand[3]
            if s % y[2] != 0:
                continue
            cand[2] = -s // y[2]
        if all(v == 0 for v in cand) or not consistent(cand):
            continue
        tests.append(cand)
    tests.append([0, 0, 0, 0])                       # trivial b = 0

    all_ok_new = True
    nonzero = 0
    task_formula_nonzero_ok = 0
    for b in tests:
        bF = [Fraction(x) for x in b]
        cond = consistent(b)
        u = [sum(Pi[i][j] * bF[j] for j in range(3)) for i in range(3)]
        xp_new = u + [Fraction(0)]
        Axp_new = matvec(M, xp_new)
        ok_new = (Axp_new == bF)
        all_ok_new = all_ok_new and cond and ok_new
        xp_old = [bF[0], bF[1], bF[2], Fraction(0)]
        Axp_old = matvec(M, xp_old)
        ok_old = (Axp_old == bF)
        if any(v != 0 for v in b):
            nonzero += 1
            if ok_old:
                task_formula_nonzero_ok += 1
        print(f"b = {b} | y^T b = {sum(y[i]*b[i] for i in range(4))} (==0: {cond})")
        print(f"   xp = (P^-1 b_top, 0) = {[str(x) for x in xp_new]}"
              f" | A @ xp = {[str(x) for x in Axp_new]} | == b: {ok_new}")
        print(f"   task's xp = (b1,b2,b3,0) | A @ xp = {[str(x) for x in Axp_old]}"
              f" | == b: {ok_old}")
    chk("correct formula xp = (P^-1 (b1,b2,b3)^T, 0) reproduces b "
        "for every consistent b tested", all_ok_new)
    chk(f"task's formula xp = (b1,b2,b3,0) FAILS for all {nonzero} nonzero "
        "consistent b tested (it only holds when b = 0)",
        task_formula_nonzero_ok == 0)

    # inconsistent b must be rejected
    bad = [1, 1, 1, 1]
    if consistent(bad):
        bad[3] += 1
    chk("an inconsistent b is correctly rejected by y^T b != 0 "
        f"(b={bad}, y^T b={sum(y[i]*bad[i] for i in range(4))})",
        not consistent(bad))

    # general solution xp + t*n
    b = tests[1]
    bF = [Fraction(x) for x in b]
    u = [sum(Pi[i][j] * bF[j] for j in range(3)) for i in range(3)]
    xp = u + [Fraction(0)]
    for t in (1, -3, 5):
        xg = [xp[i] + t * ni[i] for i in range(4)]
        assert matvec(M, xg) == bF, (t, xg)
    print("A @ (xp + t*n) == b verified exactly for t = 1, -3, 5")
    print()

    print("=== SUMMARY ===")
    print("ALL CHECKS PASSED:", ok_all)
    print("A =", M)
    print("R =", [[int(x) for x in row] for row in R])
    print("pivots =", pivots)
    print("n =", ni)
    print("y =", y)
    print("P^-1 =", [[int(x) for x in row] for row in Pi])


if __name__ == "__main__":
    main()
