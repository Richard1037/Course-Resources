"""Find a 4x4 integer rank-3 matrix with integer RREF free-column and nice left nullspace."""
import random
from fractions import Fraction as F

random.seed(4242)


def mul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]


def ident(n):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def rref_with_P(A):
    n = len(A)
    R = [r[:] for r in A]
    P = [r[:] for r in ident(n)]
    piv, r = [], 0
    for c in range(len(R[0])):
        p = next((i for i in range(r, n) if R[i][c] != 0), None)
        if p is None:
            continue
        R[r], R[p] = R[p], R[r]
        P[r], P[p] = P[p], P[r]
        pv = R[r][c]
        R[r] = [x / pv for x in R[r]]
        P[r] = [x / pv for x in P[r]]
        for i in range(n):
            if i != r and R[i][c] != 0:
                f = R[i][c]
                R[i] = [a - f * b for a, b in zip(R[i], R[r])]
                P[i] = [a - f * b for a, b in zip(P[i], P[r])]
        piv.append(c)
        r += 1
        if r == n:
            break
    return R, P, piv


def show(A):
    return [[str(x) for x in r] for r in A]


def rand_unimodular(n, ops):
    Mx = ident(n)
    for _ in range(ops):
        E = [r[:] for r in ident(n)]
        i, j = random.sample(range(n), 2)
        k = F(random.choice([-3, -2, -1, 1, 2, 3]))
        E[i][j] = k
        Mx = mul(E, Mx)
    return Mx


def build(f, U):
    """A = U @ [I3 | f ; 0...0] with f a 3-vector."""
    R0 = [[F(1), F(0), F(0), f[0]],
          [F(0), F(1), F(0), f[1]],
          [F(0), F(0), F(1), f[2]],
          [F(0), F(0), F(0), F(0)]]
    return mul(U, R0)


best = None
for trial in range(400000):
    # build A = U @ [I3 | f ; e4]  where e4 makes row 4 = row1+row2+row3+[0,0,0,s]
    # This guarantees RREF = [I3 | f] with pivots 0,1,2 and a clean xp = (b1,b2,b3,0).
    f = [F(random.randint(-4, 4)) for _ in range(3)]
    if any(x == 0 for x in f) or len(set(f)) < 2:
        continue
    s = F(random.choice([-3, -2, -1, 1, 2, 3]))
    R0 = [[F(1), F(0), F(0), f[0]],
          [F(0), F(1), F(0), f[1]],
          [F(0), F(0), F(1), f[2]],
          [F(1), F(1), F(1), F(1) + f[0] + f[1] + f[2] + s]]
    # row4 - row1 - row2 - row3 = [0,0,0,s] ; RREF of R0 is [I3|f] iff row4 depends on rows1-3
    U = rand_unimodular(4, random.randint(3, 6))
    A = mul(U, R0)
    if any(x.denominator != 1 for row in A for x in row):
        continue
    if max(abs(x) for row in A for x in row) > 9:
        continue
    if any(all(x == 0 for x in row) for row in A):
        continue
    R, P, piv = rref_with_P(A)
    if piv != [0, 1, 2] or len(piv) != 3:
        continue
    if any(x.denominator != 1 for row in R for x in row):
        continue
    if s == 0:
        continue
    y = P[3]
    if any(x.denominator != 1 or abs(x) > 5 for x in y):
        continue
    if sum(1 for x in y if x != 0) < 4:
        continue
    null = [-f[0], -f[1], -f[2], F(1)]
    if any(x.denominator != 1 or abs(x) > 8 for x in null):
        continue
    if mul(A, [[v] for v in null]) != [[F(0)] for _ in range(4)]:
        continue
    if mul([y], A) != [[F(0)] * 4]:
        continue
    rows = [[F(x) for x in r] for r in A]
    vals = [x for row in rows for x in row if x != 0]
    if all(v > 0 for v in vals) or all(v < 0 for v in vals):
        continue
    if any(all(rows[i][c] == 0 for i in range(4)) for c in range(4)):
        continue
    # xp = (b1,b2,b3,0) must always solve when y.b = 0
    tests = 0
    ok = True
    for b1 in range(-3, 4):
        for b2 in range(-3, 4):
            for b3 in range(-3, 4):
                if y[3] == 0:
                    continue
                b4 = -(y[0] * b1 + y[1] * b2 + y[2] * b3) / y[3]
                if b4.denominator != 1:
                    continue
                b = [F(b1), F(b2), F(b3), b4]
                if mul(A, [[b[0]], [b[1]], [b[2]], [F(0)]]) != [[v] for v in b]:
                    ok = False
                tests += 1
                if tests >= 30:
                    break
            if tests >= 30:
                break
        if tests >= 30:
            break
    if not ok or tests < 30:
        continue
    best = (show(rows), show(R), piv, [str(x) for x in null], [str(x) for x in y], trial, f, s)
    break

if best is None:
    print("none found")
else:
    A_s, R_s, piv, null_s, y_s, trial, f, s_extra = best
    print("trial", trial, "f =", [str(x) for x in f], "s =", str(s_extra))
    print("A =", A_s)
    print("R =", R_s, "pivots", piv)
    print("null =", null_s)
    print("y (left null) =", y_s)
    A = [[F(x) for x in r] for r in A_s]
    y = [F(x) for x in y_s]
    # particular solution xp = (b1,b2,b3,0) must satisfy A xp = b for consistent b
    tests = 0
    ok = True
    for b1 in range(-3, 4):
        for b2 in range(-3, 4):
            for b3 in range(-3, 4):
                s = y[0] * b1 + y[1] * b2 + y[2] * b3
                if y[3] == 0:
                    continue
                b4 = -s / y[3]
                if b4.denominator != 1:
                    continue
                b = [F(b1), F(b2), F(b3), b4]
                xp = [b[0], b[1], b[2], F(0)]
                if mul(A, [[v] for v in xp]) != [[v] for v in b]:
                    ok = False
                tests += 1
                if tests >= 20:
                    break
            if tests >= 20:
                break
        if tests >= 20:
            break
    print("xp=(b1,b2,b3,0) verified on %d consistent b: %s" % (tests, ok))
    # also verify the alternative xp = (b1 + f1 t, ..., 0) style is unnecessary
    bad = [F(1), F(2), F(3), F(4)]
    v = sum(y[i] * bad[i] for i in range(4))
    print("b=(1,2,3,4): y.b =", v, "->", "consistent" if v == 0 else "inconsistent")
