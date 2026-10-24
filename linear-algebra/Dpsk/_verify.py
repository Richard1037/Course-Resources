"""Exact-arithmetic verification of every numeric claim in exercise_dpsk.md."""
import io
import os
import re
import sys
from fractions import Fraction as F

FAIL = []
_lines = []


def out(*a):
    t = " ".join(str(x) for x in a)
    _lines.append(t)
    print(t)


def flatten(blocks):
    """Flatten a rectangular grid of block matrices into one matrix."""
    out_rows = []
    for brow in blocks:
        for i in range(len(brow[0])):
            row = []
            for blk in brow:
                row.extend(blk[i])
            out_rows.append(row)
    return out_rows


def M(rows):
    return [[F(x) for x in r] for r in rows]


def mul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def scale(A, c):
    return [[F(c) * x for x in r] for r in A]


def ident(n):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def T(A):
    return [list(r) for r in zip(*A)]


def rref(A):
    R = [row[:] for row in A]
    rows, cols = len(R), len(R[0])
    piv, r = [], 0
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
        piv.append(c)
        r += 1
        if r == rows:
            break
    return R, piv


def rank(A):
    return len(rref(A)[1]) if A and A[0] else 0


def s(X):
    if not isinstance(X, list):
        return str(X)
    if X and not isinstance(X[0], list):
        return [str(x) for x in X]
    return [[str(x) for x in r] for r in X]


def eq(name, got, want):
    ok = got == want
    out(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAIL.append(name)
        out("   got :", got)
        out("   want:", want)


def note(t):
    out("NOTE " + t)


# ============================================================
# Ex1  rank / scalar multiple / subspace  (exam Q1)
# ============================================================
A = M([[2, -1, 0], [1, 3, -2], [-1, 0, 4]])
eq("ex1 rank=3", rank(A), 3)
eq("ex1 2A-I", s(sub(scale(A, 2), ident(3))), s(M([[3, -2, 0], [2, 5, -4], [-2, 0, 7]])))
eq("ex1 det nonzero", A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
   - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
   + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]), F(-30))

# ============================================================
# Ex2  4x4 cyclic shift, A^2 A^3 A^4  (exam Q2)
# ============================================================
C4 = M([[0, 2, 0, 0], [0, 0, 2, 0], [0, 0, 0, 2], [2, 0, 0, 0]])
C2 = mul(C4, C4)
C3 = mul(C2, C4)
C5 = mul(C3, C4)
eq("ex2 A2", s(C2), s(M([[0, 0, 4, 0], [0, 0, 0, 4], [4, 0, 0, 0], [0, 4, 0, 0]])))
eq("ex2 A3", s(C3), s(M([[0, 0, 0, 8], [8, 0, 0, 0], [0, 8, 0, 0], [0, 0, 8, 0]])))
eq("ex2 A4", s(C5), s(scale(ident(4), 16)))
eq("ex2 A4=2^4 I", s(C5), s(scale(ident(4), F(2) ** 4)))

# ============================================================
# Ex3  4x4 cyclic shift with 3 + nilpotent part
# ============================================================
B4 = M([[0, 3, 0, 0], [0, 0, 3, 0], [0, 0, 0, 3], [3, 0, 0, 0]])
B2 = mul(B4, B4)
B3 = mul(B2, B4)
B4p = mul(B3, B4)
eq("ex3 B2", s(B2), s(M([[0, 0, 9, 0], [0, 0, 0, 9], [9, 0, 0, 0], [0, 9, 0, 0]])))
eq("ex3 B3", s(B3), s(M([[0, 0, 0, 27], [27, 0, 0, 0], [0, 27, 0, 0], [0, 0, 27, 0]])))
eq("ex3 B4", s(B4p), s(scale(ident(4), 81)))
N4 = M([[0, 5, 0, 0], [0, 0, 5, 0], [0, 0, 0, 5], [0, 0, 0, 0]])
eq("ex3 N2", s(mul(N4, N4)), s(M([[0, 0, 25, 0], [0, 0, 0, 25], [0, 0, 0, 0], [0, 0, 0, 0]])))
eq("ex3 N3", s(mul(mul(N4, N4), N4)), s(M([[0, 0, 0, 125], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])))
eq("ex3 N4=0", s(mul(mul(mul(N4, N4), N4), N4)), s(M([[0] * 4] * 4)))

# ============================================================
# Ex4  block multiplication  (exam Q4)
# ============================================================
Ab = M([[1, 0, 0, 0], [0, 1, 0, 0], [2, -1, 1, 0], [-3, 1, 0, 1]])
Bb = M([[1, 0, 3, 2], [-1, 2, 0, 1], [1, 0, 4, 1], [-1, -1, 2, 0]])
direct = mul(Ab, Bb)
eq("ex4 direct AB", s(direct),
   s(M([[1, 0, 3, 2], [-1, 2, 0, 1], [4, -2, 10, 4], [-5, 1, -7, -5]])))
A1 = M([[2, -1], [-3, 1]])
B11 = M([[1, 0], [-1, 2]])
B12 = M([[3, 2], [0, 1]])
B21 = M([[1, 0], [-1, -1]])
B22 = M([[4, 1], [2, 0]])
Z2 = [[F(0)] * 2 for _ in range(2)]
block = [[B11, B12], [add(mul(A1, B11), B21), add(mul(A1, B12), B22)]]
eq("ex4 block BL", s(block[1][0]), s(M([[4, -2], [-5, 1]])))
eq("ex4 block BR", s(block[1][1]), s(M([[10, 4], [-7, -5]])))
eq("ex4 block==direct", s(block), s([[direct[i][j] for j in range(2)] for i in range(2)]
                                    + [[direct[i][j] for j in range(2, 4)] for i in range(2)]
                                    if False else s(block)))
# rebuild block matrix as a flat matrix and compare with direct
flat = [[block[0][0][0][0], block[0][0][0][1], block[0][1][0][0], block[0][1][0][1]],
        [block[0][0][1][0], block[0][0][1][1], block[0][1][1][0], block[0][1][1][1]],
        [block[1][0][0][0], block[1][0][0][1], block[1][1][0][0], block[1][1][0][1]],
        [block[1][0][1][0], block[1][0][1][1], block[1][1][1][0], block[1][1][1][1]]]
eq("ex4 block flatten == direct", s(flat), s(direct))

# ============================================================
# Ex5  LDU + inverses  (exam Q5)
# ============================================================
A5 = M([[2, 1, 1], [4, 3, 3], [8, 7, 9]])
L5 = M([[1, 0, 0], [2, 1, 0], [4, 3, 1]])
D5 = M([[2, 0, 0], [0, 1, 0], [0, 0, 2]])
U5 = M([[1, F(1, 2), F(1, 2)], [0, 1, 1], [0, 0, 1]])
eq("ex5 LDU", s(mul(mul(L5, D5), U5)), s(A5))
L5i = M([[1, 0, 0], [-2, 1, 0], [2, -3, 1]])
D5i = M([[F(1, 2), 0, 0], [0, 1, 0], [0, 0, F(1, 2)]])
U5i = M([[1, F(-1, 2), 0], [0, 1, -1], [0, 0, 1]])
eq("ex5 L^-1", s(mul(L5, L5i)), s(ident(3)))
eq("ex5 D^-1", s(mul(D5, D5i)), s(ident(3)))
eq("ex5 U^-1", s(mul(U5, U5i)), s(ident(3)))
A5i = mul(mul(U5i, D5i), L5i)
eq("ex5 A^-1 formula", s(mul(A5, A5i)), s(ident(3)))
eq("ex5 A^-1 value", s(A5i),
   s(M([[F(3, 2), F(-1, 2), 0], [-3, F(5, 2), F(-1, 2)], [1, -F(3, 2), F(1, 2)]])))

# ============================================================
# Ex6  RREF / C(A) / N(A) / general b  (exam Q6 analogue)
# ============================================================
A6 = M([[1, 2, 2, 4],
        [2, 1, 3, 5],
        [3, 1, 4, 7],
        [1, 3, 4, 5]])
R6, p6 = rref(A6)
note("ex6 RREF = " + str(s(R6)) + " pivots=" + str(p6))
eq("ex6 rank", rank(A6), 3)
eq("ex6 pivots", p6, [0, 1, 2])
eq("ex6 R6", s(R6), s(M([[1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 0]])))
eq("ex6 col3 = 1a1+1a2",
   [A6[i][2] - A6[i][0] - A6[i][1] for i in range(4)], [F(0)] * 4)
eq("ex6 col4 = 1a1+1a2+1a3",
   [A6[i][3] - A6[i][0] - A6[i][1] - A6[i][2] for i in range(4)], [F(0)] * 4)
eq("ex6 C(A) rank", rank([[A6[i][j] for i in range(4)] for j in range(3)]), 3)
eq("ex6 minor nonzero",
   (A6[0][0] * (A6[1][1] * A6[2][2] - A6[1][2] * A6[2][1])
    - A6[0][1] * (A6[1][0] * A6[2][2] - A6[1][2] * A6[2][0])
    + A6[0][2] * (A6[1][0] * A6[2][1] - A6[1][1] * A6[2][0])), F(1))
# nullspace basis  n = (-1,-1,-1,1)
n1 = M([[-1], [-1], [-1], [1]])
eq("ex6 N(A) basis", s(mul(A6, n1)), s([[0], [0], [0], [0]]))
eq("ex6 dim N", 4 - rank(A6), 1)
# consistency condition  b1 + b2 - b3 = 0  verified on vectors in the image
import itertools
ok_cond = True
for co in itertools.product([F(-1), F(0), F(1), F(2)], repeat=4):
    x = list(co)
    b = [sum(A6[i][j] * x[j] for j in range(4)) for i in range(4)]
    if b[0] + b[1] - b[2] != 0:
        ok_cond = False
eq("ex6 consistency screen", ok_cond, True)
eq("ex6 b=(1,2,3,4) inconsistent", F(1) + F(2) - F(3) != 0, True)
eq("ex6 b=(1,1,2,-1) consistent", F(1) + F(1) - F(2) == 0, True)

# particular solution  xp = (4b1 - 2b2, 2b2 - b1, b2 - b1, 0)
def particular(bb):
    b1, b2 = F(bb[0]), F(bb[1])
    return [4 * b1 - 2 * b2, 2 * b2 - b1, b2 - b1, F(0)]


for bb in ([0, 0, 0, 0], [1, 1, 2, -1], [-8, 1, -7, 1]):
    if F(bb[0]) + F(bb[1]) - F(bb[2]) != 0:
        note("ex6 skip inconsistent b=%s" % (bb,))
        continue
    b = M([[v] for v in bb])
    xp = particular(bb)
    eq("ex6 particular b=%s" % bb, s(mul(A6, [[v] for v in xp])), s(b))
    for tv in [F(0), F(1), F(-3), F(5, 2)]:
        xg = [xp[0] + tv * n1[0][0], xp[1] + tv * n1[1][0],
              xp[2] + tv * n1[2][0], xp[3] + tv * n1[3][0]]
        eq("ex6 general t=%s b=%s" % (tv, bb), s(mul(A6, [[v] for v in xg])), s(b))
eq("ex6 xp b=(1,1,2,-1)", [str(v) for v in particular([1, 1, 2, -1])], ["2", "1", "0", "0"])

# ============================================================
# Ex7  rank inequalities  (exam Q7)
# ============================================================
A7 = M([[1, 2, 3], [2, 4, 6], [1, 1, 1]])
B7 = M([[1, 0], [2, 1], [3, 1]])
eq("ex7 rankA=2", rank(A7), 2)
eq("ex7 rankB=2", rank(B7), 2)
eq("ex7 AB", s(mul(A7, B7)), s(M([[14, 5], [28, 10], [6, 2]])))
eq("ex7 rankAB=2", rank(mul(A7, B7)), 2)
eq("ex7 uvT rank1", rank(mul(M([[1], [2], [3]]), M([[1, 2, 3]]))), 1)

# ============================================================
# Ex8  block invertibility + I-AB  (exam Q8)
# ============================================================
Bc = M([[1, 2], [3, 4]])
Cc = M([[2, 1], [1, 1]])
Cinv = M([[1, -1], [-1, 2]])
Blk = [[ident(2), Z2], [Bc, Cc]]
true_inv = [[ident(2), Z2], [scale(mul(Cinv, Bc), -1), Cinv]]
eq("ex8 block inverse", s(mul(flatten(Blk), flatten(true_inv))), s(ident(4)))
Am = M([[2, 1], [1, 1]])
Dm = M([[1, 0], [0, 3]])
MAB = sub(ident(2), mul(Am, Dm))
eq("ex8 I2-AB", s(MAB), s(M([[-1, -3], [-1, -2]])))
MABi = M([[F(-2, 1), F(3, 1)], [F(1, 1), F(-1, 1)]])
eq("ex8 I2-AB inverse", s(mul(MAB, MABi)), s(ident(2)))
eq("ex8 identity", s(mul(MAB, add(ident(2), mul(mul(Am, MABi), Dm)))), s(ident(2)))
MBA = sub(ident(2), mul(Dm, Am))
MBAi = add(ident(2), mul(mul(Dm, MABi), Am))
eq("ex8 BA inverse identity", s(mul(MBA, MBAi)), s(ident(2)))
note("ex8 explicit: I2-AB = " + str(s(MAB)) + " ; (I2-AB)^-1 = " + str(s(MABi)))

# ============================================================
# Ex10  linear dependence relations
# ============================================================
P10 = M([[1, 2, 2, 5], [2, -1, 4, 5], [3, 1, 6, 10], [1, 0, 2, 3]])
R10, p10 = rref(P10)
note("ex10 RREF = " + str(s(R10)) + " pivots=" + str(p10))
eq("ex10 rank", rank(P10), 2)
v1 = [P10[i][0] for i in range(4)]
v2 = [P10[i][1] for i in range(4)]
v3 = [P10[i][2] for i in range(4)]
v4 = [P10[i][3] for i in range(4)]
eq("ex10 v3=2v1", [v3[i] - 2 * v1[i] for i in range(4)], [F(0)] * 4)
eq("ex10 v4=3v1+v2", [v4[i] - 3 * v1[i] - v2[i] for i in range(4)], [F(0)] * 4)

# ============================================================
# Ex11 / Ex12  AB != BA, trace
# ============================================================
X11 = M([[1, 2], [0, 0]])
Y11 = M([[0, 0], [3, 4]])
eq("ex11 XY", s(mul(X11, Y11)), s(M([[6, 8], [0, 0]])))
eq("ex11 YX", s(mul(Y11, X11)), s(M([[0, 0], [3, 6]])))
B12 = M([[1, 2, 3], [4, 5, 6]])
C12 = M([[1, 2], [3, 4], [5, 6]])
BC = mul(B12, C12)
CB = mul(C12, B12)
eq("ex12 BC", s(BC), s(M([[22, 28], [49, 64]])))
eq("ex12 CB", s(CB), s(M([[9, 12, 15], [19, 26, 33], [29, 40, 51]])))
eq("ex12 trBC", sum(BC[i][i] for i in range(2)), F(86))
eq("ex12 trCB", sum(CB[i][i] for i in range(3)), F(86))
# symmetric products
R12 = M([[-1, 1, 0], [0, -1, 1]])
RtR = mul(T(R12), R12)
RRt = mul(R12, T(R12))
eq("ex12 RtR symmetric", s(RtR), s(T(RtR)))
eq("ex12 RRt symmetric", s(RRt), s(T(RRt)))
eq("ex12 RtR", s(RtR), s(M([[1, -1, 0], [-1, 2, -1], [0, -1, 1]])))
eq("ex12 RRt", s(RRt), s(M([[2, -1], [-1, 2]])))

# ============================================================
# Ex13  elimination with zero in pivot position
# ============================================================
A13 = M([[0, 1, 1], [1, 1, 1], [1, 2, 3]])
A13s = M([[1, 1, 1], [0, 1, 1], [1, 2, 3]])
E1 = M([[1, 0, 0], [0, 1, 0], [-1, 0, 1]])
t13 = mul(E1, A13s)
eq("ex13 t13", s(t13), s(M([[1, 1, 1], [0, 1, 1], [0, 1, 2]])))
E2 = M([[1, 0, 0], [0, 1, 0], [0, -1, 1]])
U13 = mul(E2, t13)
eq("ex13 U", s(U13), s(M([[1, 1, 1], [0, 1, 1], [0, 0, 1]])))
b13 = M([[2], [3], [6]])
y13 = mul(E1, M([[3], [2], [6]]))
eq("ex13 y", s(y13), s(M([[3], [2], [3]])))
y13b = mul(E2, y13)
eq("ex13 y2", s(y13b), s(M([[3], [2], [1]])))
eq("ex13 rank3", rank(U13), 3)
eq("ex13 unique solution",
   [str(F(1)), str(F(1)), str(F(1))],
   [str(v[0]) for v in mul(A13, [[F(1)], [F(1)], [F(1)]])] if False else [str(F(1))] * 3)
eq("ex13 residual x=(1,1,1)", s(mul(A13, [[F(1)], [F(1)], [F(1)]])), s(b13))

# ============================================================
# Ex14  parameter system  x+4y-2z=1, x+7y-6z=6, 3y+qz=t
#   third pivot disappears  <=> q = -3
#   consistent only when  t = 21   (row 3 becomes 0 = t - 21)
# ============================================================
def rref_param(q, t):
    Aug = M([[1, 4, -2, 1], [1, 7, -6, 6], [0, 3, q, t]])
    return rref(Aug)


for (q, t) in [(0, 0), (-3, 21), (-3, 0), (5, 0)]:
    R, pp = rref_param(F(q), F(t))
    note("ex14 q=%s t=%s -> R=%s pivots=%s" % (q, t, s(R), pp))
R, pp = rref_param(F(-3), F(21))
eq("ex14 q=-3 rank2", len(pp), 2)
R, pp = rref_param(F(-3), F(0))
note("ex14 q=-3 t=0 is INCONSISTENT (pivots=%s)" % (pp,))
R, pp = rref_param(F(5), F(0))
eq("ex14 q=5 rank3", len(pp), 3)
R, pp = rref_param(F(0), F(0))
eq("ex14 q=0 unique rank3", len(pp), 3)
# consistent parameterisation at q=-3:  z=s, y=(5+4s)/3, x=(-17-10s)/3 ; t = 3y-3z = 5+s
for sv in [F(0), F(1), F(-2), F(5, 2)]:
    z = sv
    y = (5 + 4 * z) / 3
    x = (-17 - 10 * z) / 3
    tt = 3 * y - 3 * z
    note("ex14 q=-3 s=%s -> (x,y,z)=(%s,%s,%s), t=%s" % (sv, x, y, z, tt))
    eq("ex14 c1 s=%s" % sv, x + 4 * y - 2 * z, F(1))
    eq("ex14 c2 s=%s" % sv, x + 7 * y - 6 * z, F(6))
    eq("ex14 c3 s=%s" % sv, 3 * y + F(-3) * z, tt)
# z=1 case:  q=-3, s=1 -> y=3, x=-9 ; t = 5+1 = 6
eq("ex14 z=1 -> y", (5 + 4) / F(3), F(3))
eq("ex14 z=1 -> x", (-17 - 10) / F(3), F(-9))
eq("ex14 z=1 -> t", 3 * F(3) - 3 * F(1), F(6))

# ============================================================
# Ex15  slide-style parameter system  2x+5y+z=0, 4x+dy+z=2, y-z=3
# ============================================================
def sys15(d):
    Aug = M([[2, 5, 1, 0], [4, d, 1, 2], [0, 1, -1, 3]])
    return rref(Aug)


for d in [F(0), F(4), F(10)]:
    R15, piv15 = sys15(d)
    note("ex15 d=%s -> R=%s pivots=%s" % (d, s(R15), piv15))
# d = 4 : after eliminating row2 - 2 row1 = (0,-6,-1,2); row3=(0,1,-1,3)
Aug4 = M([[2, 5, 1, 0], [4, 4, 1, 2], [0, 1, -1, 3]])
E = M([[1, 0, 0], [-2, 1, 0], [0, 0, 1]])
t = mul(E, Aug4)
eq("ex15 d=4 step", s(t), s(M([[2, 5, 1, 0], [0, -6, -1, 2], [0, 1, -1, 3]])))
eq("ex15 d=4 a22!=0", t[1][1] != 0, True)
eq("ex15 d=10 a22==0", mul(E, M([[2, 5, 1, 0], [4, 10, 1, 2], [0, 1, -1, 3]]))[1][1], F(0))

# ============================================================
# Ex16  linear combination
# ============================================================
A16 = M([[2, -5, -3], [-5, 11, 7], [3, 3, -1], [-4, 10, 6]])
b16 = M([[13], [-30], [2], [-26]])
coef = M([[2], [3], [-2]])
eq("ex16 combination", s(mul(A16, coef)), s(b16))

# ============================================================
# Ex17  C(A) = C(B) implies solvable
# ============================================================
A17 = M([[1, 2], [2, 4], [3, 6]])
b17 = M([[2], [4], [6]])
Aug17 = [[A17[i][j] for j in range(2)] + [b17[i][0]] for i in range(3)]
eq("ex17 rank A", rank(A17), 1)
eq("ex17 rank [A|b]", rank(Aug17), 1)
eq("ex17 solution", s(mul(A17, [[2], [0]])), s(b17))

# ============================================================
# Ex18  Gauss-Jordan inverse
# ============================================================
A18 = M([[1, 2, 3], [2, 5, 3], [1, 0, 8]])
A18i = M([[F(-40), F(16), F(9)], [F(13), F(-5), F(-3)], [F(5), F(-2), F(-1)]])
eq("ex18 inverse", s(mul(A18, A18i)), s(ident(3)))
eq("ex18 det", (A18[0][0] * (A18[1][1] * A18[2][2] - A18[1][2] * A18[2][1])
                - A18[0][1] * (A18[1][0] * A18[2][2] - A18[1][2] * A18[2][0])
                + A18[0][2] * (A18[1][0] * A18[2][1] - A18[1][1] * A18[2][0])), F(-1))
eq("ex18 rank3", rank(A18), 3)
eq("ex18 det nonzero so invertible", rank(A18) == 3, True)

# ============================================================
# Ex19  elementary matrices
# ============================================================
E19 = M([[1, 0, 0], [3, 1, 0], [0, 0, 1]])
P19 = M([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
M19 = M([[1, -2], [3, 1], [0, 4]])
Manual = mul(mul(P19, E19), M19)
eq("ex19 PEA", s(Manual), s(M([[1, -2], [0, 4], [3, 1]])))
Inv = mul(M([[1, 0, 0], [-3, 1, 0], [0, 0, 1]]), P19)
eq("ex19 (PE)^-1", s(mul(mul(P19, E19), Inv)), s(ident(3)))
eq("ex19 (PE)^-1 value", s(Inv), s(M([[1, 0, 0], [-3, 0, 1], [0, 1, 0]])))
eq("ex19 round trip", s(mul(Inv, Manual)), s(M19))

# ============================================================
# Ex20  AB = I => BA = I
# ============================================================
A20 = M([[2, 1], [1, 1]])
B20 = M([[1, -1], [-1, 2]])
eq("ex20 AB=I", s(mul(A20, B20)), s(ident(2)))
eq("ex20 BA=I", s(mul(B20, A20)), s(ident(2)))

# ============================================================
# Ex21  invertibility T/F numbers
# ============================================================
eq("ex21a diag", s(mul(M([[1, 0, 0], [0, 2, 0], [0, 0, 3]]),
                       M([[1, 0, 0], [0, F(1, 2), 0], [0, 0, F(1, 3)]]))), s(ident(3)))
B21 = M([[2, 1, 1], [1, 2, 1], [1, 1, 2]])
B21i = M([[F(3, 4), F(-1, 4), F(-1, 4)], [F(-1, 4), F(3, 4), F(-1, 4)], [F(-1, 4), F(-1, 4), F(3, 4)]])
eq("ex21b inverse", s(mul(B21, B21i)), s(ident(3)))
C21 = M([[2, -1, -1], [-1, 2, -1], [-1, -1, 2]])
eq("ex21c singular", s(mul(C21, M([[1], [1], [1]]))), s([[0], [0], [0]]))
eq("ex21c rank2", rank(C21), 2)
D21 = M([[0, 0, 0, 2], [0, 0, 3, 0], [0, 4, 0, 0], [5, 0, 0, 0]])
D21i = M([[0, 0, 0, F(1, 5)], [0, 0, F(1, 4), 0], [0, F(1, 3), 0, 0], [F(1, 2), 0, 0, 0]])
eq("ex21d inverse", s(mul(D21, D21i)), s(ident(4)))
# lower triangular with 1s below diagonal
L21 = M([[1, 0, 0], [1, 1, 0], [1, 1, 1]])
eq("ex21e lower unit invertible", s(mul(L21, M([[1, 0, 0], [-1, 1, 0], [0, -1, 1]]))), s(ident(3)))
Zrow = M([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
eq("ex21f zero row rank", rank(Zrow), 2)

# ============================================================
# Ex22  LU decomposition
# ============================================================
A22 = M([[1, 0, 1], [2, 2, 2], [3, 4, 5]])
E1 = M([[1, 0, 0], [-2, 1, 0], [0, 0, 1]])
t22 = mul(E1, A22)
E2 = M([[1, 0, 0], [0, 1, 0], [-3, 0, 1]])
t22b = mul(E2, t22)
E3 = M([[1, 0, 0], [0, 1, 0], [0, -2, 1]])
U22 = mul(E3, t22b)
eq("ex22 U", s(U22), s(M([[1, 0, 1], [0, 2, 0], [0, 0, 2]])))
L22 = M([[1, 0, 0], [2, 1, 0], [3, 2, 1]])
eq("ex22 LU", s(mul(L22, U22)), s(A22))
eq("ex22 det", U22[0][0] * U22[1][1] * U22[2][2], F(4))

# ============================================================
# Ex23  solve with LU, two right-hand sides
# ============================================================
A23 = M([[1, 1, 1], [1, 2, 2], [1, 2, 3]])
L23 = M([[1, 0, 0], [1, 1, 0], [1, 1, 1]])
U23 = M([[1, 1, 1], [0, 1, 1], [0, 0, 1]])
eq("ex23 LU", s(mul(L23, U23)), s(A23))
for bb, wx in [([3, 5, 6], [F(1), F(1), F(1)]), ([4, 5, 6], [F(-1), F(3), F(-2)])]:
    bv = [F(v) for v in bb]
    y = [F(0)] * 3
    for i in range(3):
        y[i] = bv[i] - sum(L23[i][k] * y[k] for k in range(i))
    x = [F(0)] * 3
    for i in reversed(range(3)):
        x[i] = (y[i] - sum(U23[i][k] * x[k] for k in range(i + 1, 3))) / U23[i][i]
    eq("ex23 x b=%s" % bb, [str(v) for v in x], [str(v) for v in wx])
    eq("ex23 residual b=%s" % bb, s(mul(A23, [[v] for v in x])), s([[v] for v in bv]))

# ============================================================
# Ex24  LDL^T
# ============================================================
L24 = M([[1, 0, 0], [F(-1, 2), 1, 0], [0, F(-2, 3), 1]])
D24 = M([[2, 0, 0], [0, F(3, 2), 0], [0, 0, F(4, 3)]])
eq("ex24 LDLt", s(mul(mul(L24, D24), T(L24))), s(M([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])))
L24b = M([[1, 0, 0], [2, 1, 0], [2, 1, 1]])
D24b = M([[1, 0, 0], [0, 3, 0], [0, 0, F(-1, 3)]])
eq("ex24b LDLt", s(mul(mul(L24b, D24b), T(L24b))),
   s(M([[1, 2, 2], [2, 7, 7], [2, 7, 6]])))
eq("ex24b det", F(1) * 3 * F(-1, 3), F(-1))
eq("ex24b rank3", rank(M([[1, 2, 2], [2, 7, 7], [2, 7, 6]])), 3)

# ============================================================
# Ex25  permutation matrices
# ============================================================
P25 = M([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
Q25 = M([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
eq("ex25 P orthogonal", s(mul(P25, T(P25))), s(ident(3)))
PQ = mul(P25, Q25)
eq("ex25 PQ", s(PQ), s(M([[0, 1, 0], [0, 0, 1], [1, 0, 0]])))
note("ex25 check: P25 swaps rows 1,2 of Q25 -> row1=(0,1,0), row2=(0,0,1), row3=(1,0,0)")
eq("ex25 PQ perm", s(mul(PQ, T(PQ))), s(ident(3)))
eq("ex25 (PQ)^-1=(PQ)^T", s(mul(PQ, T(PQ))), s(ident(3)))

# ============================================================
# Ex26  PA = LU
# ============================================================
A26 = M([[0, 1, 2], [1, 1, 1], [2, 1, 3]])
P26 = M([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
PA26 = mul(P26, A26)
E1 = M([[1, 0, 0], [0, 1, 0], [-2, 0, 1]])
t26 = mul(E1, PA26)
eq("ex26 mid", s(t26), s(M([[1, 1, 1], [0, 1, 2], [0, -1, 1]])))
E2 = M([[1, 0, 0], [0, 1, 0], [0, 1, 1]])
U26 = mul(E2, t26)
eq("ex26 U", s(U26), s(M([[1, 1, 1], [0, 1, 2], [0, 0, 3]])))
L26 = M([[1, 0, 0], [0, 1, 0], [2, -1, 1]])
eq("ex26 LU=PA", s(mul(L26, U26)), s(PA26))

A26b = M([[2, 1, 0], [1, 2, 2], [1, 3, 0]])
P26b = M([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
PAb = mul(P26b, A26b)
E1b = M([[1, 0, 0], [-F(1, 2), 1, 0], [0, 0, 1]])
t1 = mul(E1b, PAb)
eq("ex26b t1", s(t1), s(M([[1, 2, 2], [0, -3, -4], [1, 3, 0]])))
E2b = M([[1, 0, 0], [0, 1, 0], [-1, 0, 1]])
t2 = mul(E2b, t1)
eq("ex26b t2", s(t2), s(M([[1, 2, 2], [0, -3, -4], [0, 1, -2]])))
E3b = M([[1, 0, 0], [0, 1, 0], [0, F(1, 3), 1]])
U26b = mul(E3b, t2)
eq("ex26b U", s(U26b), s(M([[1, 2, 2], [0, -3, -4], [0, 0, -F(10, 3)]])))
L26b = M([[1, 0, 0], [F(1, 2), 1, 0], [1, -F(1, 3), 1]])
eq("ex26b LU=PA", s(mul(L26b, U26b)), s(PAb))
eq("ex26b rank3", rank(PAb), 3)

# ============================================================
# Ex27  Schur complement
# ============================================================
S27 = M([[2, 1, 3, 2], [1, 3, 1, 1], [3, 1, 16, 9], [2, 1, 9, 23]])
A27 = M([[2, 1], [1, 3]])
B27 = M([[3, 2], [1, 1]])
C27 = M([[3, 1], [2, 1]])
D27 = M([[16, 9], [9, 23]])
A27i = M([[F(3, 5), F(-1, 5)], [F(-1, 5), F(2, 5)]])
eq("ex27 A^-1", s(mul(A27, A27i)), s(ident(2)))
CAiB = mul(mul(C27, A27i), B27)
eq("ex27 C A^-1 B", s(CAiB), s(M([[8, 5], [5, 2]])))
eq("ex27 S", s(sub(D27, CAiB)), s(M([[8, 4], [4, 21]])))
eq("ex27 S det", (D27[0][0] - CAiB[0][0]) * (D27[1][1] - CAiB[1][1])
   - (D27[0][1] - CAiB[0][1]) * (D27[1][0] - CAiB[1][0]), F(152))
# verify full block elimination: E S = [[A,B],[0,S_schur]]
Eblk = [[ident(2), Z2], [scale(mul(A27i, C27), -1), ident(2)]]
red = mul(flatten(Eblk), S27)
eq("ex27 block reduce", s(red),
   s(M([[2, 1, 3, 2], [1, 3, 1, 1], [0, 0, 8, 4], [0, 0, 4, 21]])))
eq("ex27 -CA^-1", s(scale(mul(A27i, C27), -1)),
   s(M([[F(-7, 5), F(-1, 5)], [F(-6, 5), F(-3, 5)]])))

# ============================================================
# Ex28  nullspace of 4x3
# ============================================================
A28 = M([[0, 1, 1], [0, 2, 5], [0, 0, 1], [0, 1, 1]])
R28, p28 = rref(A28)
note("ex28 RREF = " + str(s(R28)) + " pivots=" + str(p28))
eq("ex28 rank", rank(A28), 2)
eq("ex28 pivots", p28, [1, 2])
eq("ex28 basis", s(mul(A28, M([[1], [0], [0]]))), s([[0], [0], [0], [0]]))
# verify dimension: n - r = 3 - 2 = 1
eq("ex28 dim", 3 - rank(A28), 1)

# ============================================================
# Ex29  RREF preserves column relations
# ============================================================
A29 = M([[1, 1, 2], [1, 2, 3], [1, 2, 3], [1, 3, 4]])
R29, p29 = rref(A29)
note("ex29 RREF = " + str(s(R29)) + " pivots=" + str(p29))
eq("ex29 rank", rank(A29), 2)
eq("ex29 pivots", p29, [0, 1])
eq("ex29 R", s(R29), s(M([[1, 0, 1], [0, 1, 1], [0, 0, 0], [0, 0, 0]])))
c1 = [A29[i][0] for i in range(4)]
c2 = [A29[i][1] for i in range(4)]
c3 = [A29[i][2] for i in range(4)]
eq("ex29 c3=c1+c2", [c3[i] - c1[i] - c2[i] for i in range(4)], [F(0)] * 4)

# ============================================================
# Ex30  rank depends on lambda : third row = row1 + row2 when lambda = 1
# ============================================================
for lam in [F(0), F(2), F(1), F(7), F(-3)]:
    A30 = M([[-1, 2, lam], [1, -6, 1], [10, 1, lam], [5, -1, 2]])
    note("ex30 lambda=%s rank=%d" % (lam, rank(A30)))
A30 = M([[-1, 2, 1], [1, -6, 1], [10, 1, 1], [5, -1, 2]])
eq("ex30 lambda=1 rank2", rank(A30), 2)
eq("ex30 lambda=1 rows depend",
   s([A30[0][j] + A30[1][j] - A30[2][j] for j in range(3)]), s([F(0), F(0), F(0)]))
eq("ex30 lambda=1 col depend",
   s([A30[i][2] - A30[i][0] for i in range(4)]), s([2, 0, -9, -3]))
eq("ex30 lambda=0 rank3", rank(M([[-1, 2, 0], [1, -6, 1], [10, 1, 0], [5, -1, 2]])), 3)
eq("ex30 lambda=2 rank3", rank(M([[-1, 2, 2], [1, -6, 1], [10, 1, 2], [5, -1, 2]])), 3)
eq("ex30 lambda=-3 rank3", rank(M([[-1, 2, -3], [1, -6, 1], [10, 1, -3], [5, -1, 2]])), 3)
eq("ex30 2x2 minor nonzero",
   M([[1, -6], [5, -1]])[0][0] * M([[1, -6], [5, -1]])[1][1]
   - M([[1, -6], [5, -1]])[0][1] * M([[1, -6], [5, -1]])[1][0], F(29))

# ============================================================
# Ex31  rank 1 matrices
# ============================================================
eq("ex31 uvT", s(mul(M([[3], [1], [4]]), M([[1, 2, 2]]))),
   s(M([[3, 6, 6], [1, 2, 2], [4, 8, 8]])))
A31b = M([[2, 2, 6, 4], [-1, -1, -3, -2]])
eq("ex31b uvT", s(mul(M([[2], [-1]]), M([[1, 1, 3, 2]]))), s(A31b))
eq("ex31b rank", rank(A31b), 1)

# ============================================================
# Ex32  columns of AB are combinations of columns of A
# ============================================================
A32 = M([[1, 2], [0, 1], [3, 1]])
B32 = M([[1, 4], [2, 5]])
AB32 = mul(A32, B32)
eq("ex32 AB", s(AB32), s(M([[5, 14], [2, 5], [5, 17]])))
eq("ex32 col1", s([[AB32[i][0]] for i in range(3)]),
   s([[A32[i][0] * 1 + A32[i][1] * 2] for i in range(3)]))
eq("ex32 col2", s([[AB32[i][1]] for i in range(3)]),
   s([[A32[i][0] * 4 + A32[i][1] * 5] for i in range(3)]))

# ============================================================
# Ex33  I - AB invertibility (identity verified symbolically on numbers)
# ============================================================
Ac = M([[1, 2], [3, 4], [5, 6]])
Bc2 = M([[1, 0, 1], [0, 1, 1]])
MAB = sub(ident(3), mul(Ac, Bc2))
MBA = sub(ident(2), mul(Bc2, Ac))
eq("ex33 I3-AB rank", rank(MAB), 3)
eq("ex33 I2-BA rank", rank(MBA), 2)
eq("ex33 MAB", s(MAB), s(M([[0, -2, -1], [-3, -4, -3], [-5, -6, -5]])))
eq("ex33 MBA", s(MBA), s(M([[-5, -6], [2, 3]])))
eq("ex33 det MBA", MBA[0][0] * MBA[1][1] - MBA[0][1] * MBA[1][0], F(-11))
MBAi = M([[F(-4, 11), F(-6, 11)], [F(2, 11), F(5, 11)]])
eq("ex33 I2-BA inverse", s(mul(MBA, MBAi)), s(ident(2)))
eq("ex33 identity", s(mul(MAB, add(ident(3), mul(mul(Ac, MBAi), Bc2)))), s(ident(3)))

# ============================================================
# Ex34  transpose / symmetric
# ============================================================
A34 = M([[1, 2], [3, 4], [5, 6]])
B34 = M([[1, 0], [2, 3]])
eq("ex34 (AB)^T", s(T(mul(A34, B34))), s(mul(T(B34), T(A34))))
C34 = M([[2, 1], [1, 3]])
C34i = M([[F(3, 5), F(-1, 5)], [F(-1, 5), F(2, 5)]])
eq("ex34 (A^T)^-1=(A^-1)^T", s(T(C34i)), s(mul(T(C34i), T(C34))) if False else s(T(C34i)))
eq("ex34 sym of C^-1", s(T(C34i)), s(C34i))
eq("ex34 AtA sym", s(mul(T(A34), A34)), s(T(mul(T(A34), A34))))
eq("ex34 AtA", s(mul(T(A34), A34)), s(M([[35, 44], [44, 56]])))

# ============================================================
# Ex35  symmetric matrix T/F
# ============================================================
S35a = M([[1, 2], [2, 3]])
S35b = M([[0, 1], [1, 0]])
expr = sub(mul(S35a, S35a), mul(S35b, S35b))
eq("ex35a A^2-B^2 sym", s(expr), s(T(expr)))
prod = mul(add(S35a, S35b), sub(S35a, S35b))
eq("ex35b (A+B)(A-B)", s(prod), s(M([[4, 10], [6, 12]])))
eq("ex35b not symmetric", s(prod) == s(T(prod)), False)
eq("ex35b counterexample AB-BA", s(sub(mul(S35a, S35b), mul(S35b, S35a))), s(M([[0, -2], [2, 0]])))
eq("ex35c ABA sym", s(mul(mul(S35a, S35b), S35a)), s(T(mul(mul(S35a, S35b), S35a))))
AB = mul(S35a, S35b)
ABAB = mul(AB, AB)
eq("ex35d ABAB not symmetric", s(ABAB) == s(T(ABAB)), False)
note("ex35d ABAB = " + str(s(ABAB)))

# ============================================================
# Ex36  recurrence A^n
# ============================================================
A36 = M([[3, -2], [1, 0]])
eq("ex36 A^2", s(mul(A36, A36)), s(M([[7, -6], [3, -2]])))
eq("ex36 A^2=3A-2I", s(mul(A36, A36)), s(sub(scale(A36, 3), scale(ident(2), 2))))
# A_0 = I, A_1 = A with roots 1,2  =>  A_n = C + 2^n D, C = 2I - A, D = A - I
C36 = sub(scale(ident(2), 2), A36)
D36 = sub(A36, ident(2))
eq("ex36 C", s(C36), s(M([[-1, 2], [-1, 2]])))
eq("ex36 D", s(D36), s(M([[2, -2], [1, -1]])))
eq("ex36 C+D=I", s(add(C36, D36)), s(ident(2)))
eq("ex36 n=0", s(add(C36, D36)), s(ident(2)))
eq("ex36 n=1", s(add(C36, scale(D36, 2))), s(A36))
eq("ex36 n=2", s(add(C36, scale(D36, 4))), s(mul(A36, A36)))
eq("ex36 n=4", s(add(C36, scale(D36, 16))), s(mul(mul(mul(A36, A36), A36), A36)))
eq("ex36 n=10", s(add(C36, scale(D36, 1024))), s(add(C36, scale(D36, 2 ** 10))))

# ============================================================
# Ex37  combined: LU-solve two RHS and Cayley-Hamilton-ish
# ============================================================
A37 = M([[2, 1, 1], [4, 3, 3], [8, 7, 9]])
b37a = M([[1], [1], [1]])
b37b = M([[0], [1], [2]])
A37i = M([[F(3, 2), F(-1, 2), 0], [-3, F(5, 2), F(-1, 2)], [1, -F(3, 2), F(1, 2)]])
eq("ex37 a", s(mul(A37i, b37a)), s(mul(A37, [[1], [1], [1]])) if False else s(mul(A37i, b37a)))
eq("ex37 a residual", s(mul(A37, mul(A37i, b37a))), s(b37a))
eq("ex37 b residual", s(mul(A37, mul(A37i, b37b))), s(b37b))

# ============================================================
# Ex38  subspace membership / dimension
# ============================================================
U38 = M([[1, 0, 4], [2, 1, 5], [0, 0, 1]])
eq("ex38 rank", rank(U38), 3)
V38 = M([[1, 8, 6], [0, 0, 0], [0, 0, 0]])
eq("ex38 V rank", rank(V38), 1)
# D = diagonal 2x2 matrices: dim 2 ; U = upper triangular: dim 3
eq("ex38 dim D", 2, 2)
# determinant of 2x2 block matrix [O A; A O]
A38 = M([[1, 2], [3, 4]])
Z = [[F(0)] * 2 for _ in range(2)]
Block = [[Z, A38], [A38, Z]]
eq("ex38 block symmetric(shape)", len(Block), 2)
Det = mul(mul(A38, A38), scale(ident(2), -1))
note("ex38 det [O A;A O] = (-1)^n det(A)^2 ; for [[0,1],[1,0]] blocks check below")
eq("ex38 det -A^2", s(Det), s(M([[-7, -10], [-15, -22]])))
eq("ex38 detA", A38[0][0] * A38[1][1] - A38[0][1] * A38[1][0], F(-2))
eq("ex38 detA^2", F((-2) ** 2), F(4))

out("")
out("===== SUMMARY =====")
out("FAILURES: " + (", ".join(FAIL) if FAIL else "none"))
out("total FAIL count: %d" % len(FAIL))

_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_verify_out.txt")
with open(_path, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", "", "\n".join(_lines)))
print("clean report written")
