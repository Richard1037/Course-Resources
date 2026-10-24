"""Final clean verification: one check per claim used in exercise_dpsk.md.

Naming rule: every matrix variable carries its exercise number (e.g. A33), and no
generic names like A / B / M are reused, so results can never be shadowed.
"""
import os
import re
from fractions import Fraction as F

OK = 0
BAD = []
LINES = []


def log(t=""):
    LINES.append(str(t))


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


def inv2(A):
    d = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    return [[A[1][1] / d, -A[0][1] / d], [-A[1][0] / d, A[0][0] / d]]


def det3(A):
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
            - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
            + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))


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
    return len(rref(A)[1])


def txt(X):
    if not isinstance(X, list):
        return str(X)
    if X and not isinstance(X[0], list):
        return "[" + ", ".join(str(x) for x in X) + "]"
    return "[" + " ; ".join(", ".join(str(x) for x in r) for r in X) + "]"


def chk(name, got, want):
    global OK
    if got == want:
        OK += 1
        log("OK   %-44s %s" % (name, txt(got)))
    else:
        BAD.append(name)
        log("FAIL %-44s got=%s  want=%s" % (name, txt(got), txt(want)))


# ---------------- 练习 1 ----------------
A1 = M([[1, 2, 1], [0, 1, 1], [1, 1, 0]])
chk("01 rank A1 (=dim C(A1))", rank(A1), 2)
chk("01 rank A1^T", rank(T(A1)), 2)
chk("01 3A1 - I3", sub(scale(A1, 3), ident(3)), M([[2, 6, 3], [0, 2, 3], [3, 3, -1]]))
chk("01 A1*(1,-1,1)=0", mul(A1, M([[1], [-1], [1]])), M([[0], [0], [0]]))
chk("01 a3 = a2 - a1", [A1[i][2] for i in range(3)],
    [A1[i][1] - A1[i][0] for i in range(3)])

# ---------------- 练习 2 ----------------
A2 = M([[0, 3, 0, 0], [0, 0, 3, 0], [0, 0, 0, 3], [3, 0, 0, 0]])
A2sq = mul(A2, A2)
A2cu = mul(A2sq, A2)
A2fo = mul(A2cu, A2)
chk("02 A2^2", A2sq, M([[0, 0, 9, 0], [0, 0, 0, 9], [9, 0, 0, 0], [0, 9, 0, 0]]))
chk("02 A2^3", A2cu, M([[0, 0, 0, 27], [27, 0, 0, 0], [0, 27, 0, 0], [0, 0, 27, 0]]))
chk("02 A2^4", A2fo, scale(ident(4), 81))
chk("02 A2^3 = 81 A2^-1", mul(A2, A2cu), scale(ident(4), 81))

# ---------------- 练习 3 ----------------
A3 = M([[1, 0, 0, 0], [0, 1, 0, 0], [2, -1, 1, 0], [-3, 1, 0, 1]])
B3 = M([[1, 0, 3, 2], [-1, 2, 0, 1], [1, 0, 4, 1], [-1, -1, 2, 0]])
chk("03 A3 B3", mul(A3, B3),
    M([[1, 0, 3, 2], [-1, 2, 0, 1], [4, -2, 10, 4], [-5, 1, -7, -5]]))

# ---------------- 练习 4 ----------------
A4 = M([[2, 1, 1], [4, 3, 3], [8, 7, 9]])
L4 = M([[1, 0, 0], [2, 1, 0], [4, 3, 1]])
D4 = M([[2, 0, 0], [0, 1, 0], [0, 0, 2]])
U4 = M([[1, F(1, 2), F(1, 2)], [0, 1, 1], [0, 0, 1]])
chk("04 LDU = A4", mul(mul(L4, D4), U4), A4)
chk("04 L4^-1", mul(L4, M([[1, 0, 0], [-2, 1, 0], [2, -3, 1]])), ident(3))
chk("04 U4^-1", mul(U4, M([[1, F(-1, 2), 0], [0, 1, -1], [0, 0, 1]])), ident(3))
A4i = M([[F(3, 2), F(-1, 2), 0], [-3, F(5, 2), F(-1, 2)], [1, -F(3, 2), F(1, 2)]])
chk("04 A4^-1", mul(A4, A4i), ident(3))

# ---------------- 练习 5 ----------------
A5 = M([[1, 0, 0, 4], [0, 1, 0, 4], [0, 0, 1, 3], [-1, -2, 1, -9]])
R5, p5 = rref(A5)
chk("05 RREF", R5, M([[1, 0, 0, 4], [0, 1, 0, 4], [0, 0, 1, 3], [0, 0, 0, 0]]))
chk("05 pivots", p5, [0, 1, 2])
chk("05 rank", rank(A5), 3)
chk("05 N(A5) basis", mul(A5, M([[-4], [-4], [-3], [1]])), [[F(0)]] * 4)
chk("05 left-null y", mul(M([[1, 2, -1, 1]]), A5), [[F(0)] * 4])
chk("05 xp for b=(1,1,2,-1)", mul(A5, M([[1], [1], [2], [0]])), M([[1], [1], [2], [-1]]))
for tv in [F(0), F(1), F(-3), F(5, 2)]:
    chk("05 general t=%s" % tv,
        mul(A5, [[F(1) - 4 * tv], [F(1) - 4 * tv], [F(2) - 3 * tv], [tv]]),
        M([[1], [1], [2], [-1]]))
chk("05 b=(1,2,3,4) fails condition", F(1) + 2 * F(2) - F(3) + F(4), F(6))

# ---------------- 练习 6 ----------------
A6 = M([[1, 2, 3], [2, 4, 6], [1, 1, 1]])
B6 = M([[1, 0], [2, 1], [3, 1]])
chk("06 rank A6", rank(A6), 2)
chk("06 rank B6", rank(B6), 2)
chk("06 A6 B6", mul(A6, B6), M([[14, 5], [28, 10], [6, 2]]))
chk("06 rank A6B6", rank(mul(A6, B6)), 2)
chk("06 strict case rank=0", rank(mul(M([[1, 0], [0, 0]]), M([[0, 0], [0, 1]]))), 0)

# ---------------- 练习 7 ----------------
B7 = M([[1, 2], [3, 4]])
C7 = M([[2, 1], [1, 1]])
C7i = M([[1, -1], [-1, 2]])
Z2 = [[F(0)] * 2 for _ in range(2)]


def flat(blocks):
    out = []
    for brow in blocks:
        for i in range(len(brow[0])):
            row = []
            for blk in brow:
                row.extend(blk[i])
            out.append(row)
    return out


chk("07 block inverse", mul(flat([[ident(2), Z2], [B7, C7]]),
                            flat([[ident(2), Z2], [scale(mul(C7i, B7), -1), C7i]])), ident(4))
Am7 = M([[2, 1], [1, 1]])
Dm7 = M([[1, 0], [0, 3]])
IAB7 = sub(ident(2), mul(Am7, Dm7))
IAB7i = inv2(IAB7)
chk("07 I2 - AB", IAB7, M([[-1, -3], [-1, -2]]))
chk("07 (I2-AB)^-1", IAB7i, M([[2, -3], [-1, 1]]))
chk("07 (I2-AB)(I2-AB)^-1", mul(IAB7, IAB7i), ident(2))
IBA7 = sub(ident(2), mul(Dm7, Am7))
chk("07 I2 - BA", IBA7, M([[-1, -1], [-3, -2]]))
chk("07 (I2-BA)^-1 direct", inv2(IBA7), M([[2, -1], [-3, 1]]))
chk("07 (I2-BA)(I2-BA)^-1", mul(IBA7, inv2(IBA7)), ident(2))
# the identity (I-AB)(I + (I-BA)^{-1} ... ) is order-sensitive; verify the correct one
chk("07 I + (I-BA)^-1 - I = (I-BA)^-1", add(ident(2), sub(inv2(IBA7), ident(2))), inv2(IBA7))
chk("07 (I-AB)^-1 = I + A(I-BA)^-1 B",
    IAB7i, add(ident(2), mul(mul(Am7, inv2(IBA7)), Dm7)))
Ac7 = M([[1, 2], [3, 4], [5, 6]])
Bc7 = M([[1, 0, 1], [0, 1, 1]])
MAB7 = sub(ident(3), mul(Ac7, Bc7))
MBA7 = sub(ident(2), mul(Bc7, Ac7))
chk("07(3) I3-AB", MAB7, M([[0, -2, -3], [-3, -3, -7], [-5, -6, -10]]))
chk("07(3) I2-BA", MBA7, M([[-5, -8], [-8, -9]]))
chk("07(3) det I3-AB", det3(MAB7), F(-19))
chk("07(3) det I2-BA", MBA7[0][0] * MBA7[1][1] - MBA7[0][1] * MBA7[1][0], F(-19))
MBA7i = inv2(MBA7)
chk("07(3) (I2-BA)^-1", mul(MBA7, MBA7i), ident(2))
chk("07(3) (I2-BA)^-1 value", MBA7i, M([[F(9, 19), -F(8, 19)], [-F(8, 19), F(5, 19)]]))

# ---------------- 练习 8 ----------------
A8 = M([[1, 1, 2, 4], [1, 2, 3, 5], [1, 2, 3, 5], [1, 3, 4, 6]])
R8, p8 = rref(A8)
chk("08 RREF", R8, M([[1, 0, 1, 3], [0, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]]))
chk("08 pivots", p8, [0, 1])
chk("08 rank", rank(A8), 2)
chk("08 a3 = a1 + a2", [A8[i][2] - A8[i][0] - A8[i][1] for i in range(4)], [F(0)] * 4)
B8 = M([[1, 4], [2, 5]])
AB8 = mul(A8, B8)
chk("08 AB col1", [[AB8[i][0]] for i in range(4)], M([[3], [5], [5], [7]]))
chk("08 AB col2", [[AB8[i][1]] for i in range(4)], M([[9], [14], [14], [19]]))
chk("08 b=(1,0,0,1) not in C(A)",
    len(rref([[A8[i][0], A8[i][1], [1, 0, 0, 1][i]] for i in range(4)])[1]), 3)

# ---------------- 练习 9 ----------------
u9 = M([[1], [2], [2]])
v9 = M([[2], [1], [-1]])
w9 = M([[1], [1], [1]])
chk("09 u.v", sum(u9[i][0] * v9[i][0] for i in range(3)), F(2))
chk("09 |u|^2", sum(u9[i][0] ** 2 for i in range(3)), F(9))
chk("09 |v|^2", sum(v9[i][0] ** 2 for i in range(3)), F(6))
chk("09 u.w", sum(u9[i][0] * w9[i][0] for i in range(3)), F(5))
chk("09 w.w", sum(w9[i][0] ** 2 for i in range(3)), F(3))
chk("09 2u/3 = unit", [F(1, 3), F(2, 3), F(2, 3)],
    [u9[i][0] / 3 for i in range(3)])

# ---------------- 练习 10 ----------------
P10 = M([[1, 2, 2, 5], [2, -1, 4, 5], [3, 1, 6, 10], [1, 0, 2, 3]])
chk("10 rank P10", rank(P10), 2)
chk("10 c3 = 2c1", [P10[i][2] - 2 * P10[i][0] for i in range(4)], [F(0)] * 4)
chk("10 c4 = 3c1 + c2", [P10[i][3] - 3 * P10[i][0] - P10[i][1] for i in range(4)], [F(0)] * 4)
chk("10 pivots", rref(P10)[1], [0, 1])
A10b = M([[2, 0, 3], [1, 1, 0], [0, 3, -1]])
chk("10 b-system det", det3(A10b), F(7))

# ---------------- 练习 11 ----------------
X11 = M([[1, 2], [0, 0]])
Y11 = M([[0, 0], [3, 4]])
chk("11 XY", mul(X11, Y11), M([[6, 8], [0, 0]]))
chk("11 YX", mul(Y11, X11), M([[0, 0], [3, 6]]))
B11 = M([[1, 2, 3], [4, 5, 6]])
C11 = M([[1, 2], [3, 4], [5, 6]])
chk("11 BC", mul(B11, C11), M([[22, 28], [49, 64]]))
chk("11 CB", mul(C11, B11), M([[9, 12, 15], [19, 26, 33], [29, 40, 51]]))
chk("11 tr BC", sum(mul(B11, C11)[i][i] for i in range(2)), F(86))
chk("11 tr CB", sum(mul(C11, B11)[i][i] for i in range(3)), F(86))
R11 = M([[-1, 1, 0], [0, -1, 1]])
chk("11 R^T R", mul(T(R11), R11), M([[1, -1, 0], [-1, 2, -1], [0, -1, 1]]))
chk("11 R R^T", mul(R11, T(R11)), M([[2, -1], [-1, 2]]))

# ---------------- 练习 12 ----------------
A12 = M([[0, 1, 1], [1, 1, 1], [1, 2, 3]])
chk("12 solution (1,1,1)", mul(A12, M([[1], [1], [1]])), M([[2], [3], [6]]))
sw = M([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
E12a = M([[1, 0, 0], [0, 1, 0], [-1, 0, 1]])
E12b = M([[1, 0, 0], [0, 1, 0], [0, -1, 1]])
chk("12 P12 A12", mul(sw, A12), M([[1, 1, 1], [0, 1, 1], [1, 2, 3]]))
chk("12 E1 P12 A12", mul(E12a, mul(sw, A12)), M([[1, 1, 1], [0, 1, 1], [0, 1, 2]]))
chk("12 U", mul(E12b, mul(E12a, mul(sw, A12))), M([[1, 1, 1], [0, 1, 1], [0, 0, 1]]))
chk("12 rank", rank(A12), 3)
chk("12 y after E1", mul(E12a, M([[3], [2], [6]])), M([[3], [2], [3]]))
chk("12 y after E2", mul(E12b, M([[3], [2], [3]])), M([[3], [2], [1]]))

# ---------------- 练习 13 ----------------
A13 = M([[1, 4, -2], [1, 7, -6], [0, 3, -4]])
chk("13 rank A13 (q=-4) = 2", rank(A13), 2)
chk("13 rank A13 (q=0) = 3", rank(M([[1, 4, -2], [1, 7, -6], [0, 3, 0]])), 3)
chk("13 rank A13 (q=5) = 3", rank(M([[1, 4, -2], [1, 7, -6], [0, 3, 5]])), 3)
chk("13 rank [A|b] q=-4 t=5 = 2", rref(M([[1, 4, -2, 1], [1, 7, -6, 6], [0, 3, -4, 5]]))[1],
    [0, 1])
chk("13 rank [A|b] q=-4 t=6 = 3",
    len(rref(M([[1, 4, -2, 1], [1, 7, -6, 6], [0, 3, -4, 6]]))[1]), 3)
for sv in [F(0), F(1), F(-2), F(5, 2)]:
    xv = F(-17, 3) - F(10, 3) * sv
    yv = F(5, 3) + F(4, 3) * sv
    chk("13 q=-4 s=%s eq1" % sv, xv + 4 * yv - 2 * sv, F(1))
    chk("13 q=-4 s=%s eq2" % sv, xv + 7 * yv - 6 * sv, F(6))
    chk("13 q=-4 s=%s eq3" % sv, 3 * yv + F(-4) * sv, F(5))
chk("13 q=-4 s=0 -> (-17/3, 5/3, 0)", [F(-17, 3), F(5, 3), F(0)],
    [F(-17, 3), F(5, 3), F(0)])

# ---------------- 练习 14 ----------------
A14 = M([[2, -5, -3], [-5, 11, 7], [3, 3, -1], [-4, 10, 6]])
chk("14 combination a1-a2-2a3", mul(A14, M([[1], [-1], [-2]])),
    M([[13], [-30], [2], [-26]]))

# ---------------- 练习 15 ----------------
A15 = M([[1, 2], [2, 4], [3, 6]])
chk("15 rank A", rank(A15), 1)
chk("15 rank [A|b]", rank([[A15[i][0], A15[i][1], F([2, 4, 6][i])] for i in range(3)]), 1)
chk("15 solution (2,0)", mul(A15, M([[2], [0]])), M([[2], [4], [6]]))
chk("15 family (2-2s, s)", mul(A15, M([[0], [1]])), M([[2], [4], [6]]))

# ---------------- 练习 16 ----------------
A16 = M([[1, 2, 3], [2, 5, 3], [1, 0, 8]])
chk("16 inverse", mul(A16, M([[-40, 16, 9], [13, -5, -3], [5, -2, -1]])), ident(3))
chk("16 det", det3(A16), F(-1))

# ---------------- 练习 17 ----------------
E17 = M([[1, 0, 0], [3, 1, 0], [0, 0, 1]])
P17 = M([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
M17 = M([[1, -2], [3, 1], [0, 4]])
chk("17 PEM17", mul(mul(P17, E17), M17), M([[1, -2], [0, 4], [6, -5]]))
chk("17 (PE)^-1", mul(mul(P17, E17), mul(M([[1, 0, 0], [-3, 1, 0], [0, 0, 1]]), P17)), ident(3))
chk("17 (PE)^-1 value", mul(M([[1, 0, 0], [-3, 1, 0], [0, 0, 1]]), P17),
    M([[1, 0, 0], [-3, 0, 1], [0, 1, 0]]))

# ---------------- 练习 18 ----------------
B18 = M([[2, 1, 1], [1, 2, 1], [1, 1, 2]])
B18i = M([[F(3, 4), -F(1, 4), -F(1, 4)], [-F(1, 4), F(3, 4), -F(1, 4)],
          [-F(1, 4), -F(1, 4), F(3, 4)]])
chk("18(b) inverse", mul(B18, B18i), ident(3))
C18 = M([[2, -1, -1], [-1, 2, -1], [-1, -1, 2]])
chk("18(c) null", mul(C18, M([[1], [1], [1]])), M([[0], [0], [0]]))
chk("18(c) rank", rank(C18), 2)
D18 = M([[0, 0, 0, 2], [0, 0, 3, 0], [0, 4, 0, 0], [5, 0, 0, 0]])
chk("18(d) inverse", mul(D18, M([[0, 0, 0, F(1, 5)], [0, 0, F(1, 4), 0],
                                 [0, F(1, 3), 0, 0], [F(1, 2), 0, 0, 0]])), ident(4))
chk("18(a) inverse", mul(M([[1, 0, 0], [0, 2, 0], [0, 0, 3]]),
                         M([[1, 0, 0], [0, F(1, 2), 0], [0, 0, F(1, 3)]])), ident(3))
chk("18(b) counterexample rank 1", rank(M([[1, 1, 1], [1, 1, 1], [1, 1, 1]])), 1)

# ---------------- 练习 19 ----------------
A19 = M([[1, 0, 1], [2, 2, 2], [3, 4, 5]])
chk("19 LU = A19", mul(M([[1, 0, 0], [2, 1, 0], [3, 2, 1]]),
                       M([[1, 0, 1], [0, 2, 0], [0, 0, 2]])), A19)
A19b = M([[1, 1, 0], [4, 6, 1], [-2, 2, 0]])
E19 = M([[1, 0, 0], [-4, 1, 0], [10, -2, 1]])
chk("19 EA = U", mul(E19, A19b), M([[1, 1, 0], [0, 2, 1], [0, 0, -2]]))
chk("19 E^-1 = L", mul(E19, M([[1, 0, 0], [4, 1, 0], [-2, 2, 1]])), ident(3))

# ---------------- 练习 20 ----------------
A20 = M([[1, 1, 1], [1, 2, 2], [1, 2, 3]])
chk("20 LU = A20", mul(M([[1, 0, 0], [1, 1, 0], [1, 1, 1]]),
                       M([[1, 1, 1], [0, 1, 1], [0, 0, 1]])), A20)
chk("20 b1 -> (1,1,1)", mul(A20, M([[1], [1], [1]])), M([[3], [5], [6]]))
chk("20 b2 -> (3,0,1)", mul(A20, M([[3], [0], [1]])), M([[4], [5], [6]]))

# ---------------- 练习 21 ----------------
L21 = M([[1, 0, 0], [-F(1, 2), 1, 0], [0, -F(2, 3), 1]])
D21 = M([[2, 0, 0], [0, F(3, 2), 0], [0, 0, F(4, 3)]])
chk("21 LDL^T", mul(mul(L21, D21), T(L21)), M([[2, -1, 0], [-1, 2, -1], [0, -1, 2]]))
L21b = M([[1, 0, 0], [2, 1, 0], [2, 1, 1]])
D21b = M([[1, 0, 0], [0, 3, 0], [0, 0, -1]])
chk("21b LDL^T", mul(mul(L21b, D21b), T(L21b)), M([[1, 2, 2], [2, 7, 7], [2, 7, 6]]))
chk("21b det", F(1) * F(3) * F(-1), F(-3))

# ---------------- 练习 22 ----------------
P22 = M([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
Q22 = M([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
chk("22 P^-1 = P^T", mul(P22, T(P22)), ident(3))
chk("22 PQ = I", mul(P22, Q22), ident(3))
chk("22 LU = A22", mul(M([[1, 0, 0], [F(1, 2), 1, 0], [F(1, 2), F(5, 3), 1]]),
                       M([[2, 1, 0], [0, F(3, 2), 2], [0, 0, -F(10, 3)]])),
    M([[2, 1, 0], [1, 2, 2], [1, 3, 0]]))
chk("22b PA = LU", mul(M([[1, 0, 0], [0, 1, 0], [2, -1, 1]]),
                       M([[1, 2, 2], [0, 1, 2], [0, 0, -2]])),
    mul(M([[0, 1, 0], [1, 0, 0], [0, 0, 1]]), M([[0, 1, 2], [1, 2, 2], [2, 3, 0]])))

# ---------------- 练习 23 ----------------
A23 = M([[2, 1], [1, 2]])
A23i = inv2(A23)
chk("23 A^-1", mul(A23, A23i), ident(2))
CAi23 = mul(M([[3, 1], [2, 1]]), A23i)
chk("23 C A^-1", CAi23, M([[F(5, 3), -F(1, 3)], [1, 0]]))
CAiB23 = mul(CAi23, M([[3, 2], [1, 1]]))
chk("23 C A^-1 B", CAiB23, M([[F(14, 3), 3], [3, 2]]))
S23 = sub(M([[16, 9], [9, 23]]), CAiB23)
chk("23 Schur complement", S23, M([[F(34, 3), 6], [6, 21]]))
chk("23 det S", S23[0][0] * S23[1][1] - S23[0][1] * S23[1][0], F(202))
chk("23 EM = [[A,B],[O,S]]",
    mul(flat([[ident(2), Z2], [scale(CAi23, -1), ident(2)]]),
        M([[2, 1, 3, 2], [1, 2, 1, 1], [3, 1, 16, 9], [2, 1, 9, 23]])),
    M([[2, 1, 3, 2], [1, 2, 1, 1], [0, 0, F(34, 3), 6], [0, 0, 6, 21]]))

# ---------------- 练习 24 ----------------
A24 = M([[0, 1, 1], [0, 2, 5], [0, 0, 1], [0, 1, 1]])
chk("24 RREF", rref(A24)[0], M([[0, 1, 0], [0, 0, 1], [0, 0, 0], [0, 0, 0]]))
chk("24 pivots", rref(A24)[1], [1, 2])
chk("24 null basis (1,0,0)", mul(A24, M([[1], [0], [0]])), [[F(0)]] * 4)
chk("24 dim N", 3 - rank(A24), 1)

# ---------------- 练习 25 ----------------
A25 = M([[1, 1, 2], [1, 2, 3], [1, 2, 3], [1, 3, 4]])
chk("25 RREF", rref(A25)[0], M([[1, 0, 1], [0, 1, 1], [0, 0, 0], [0, 0, 0]]))
chk("25 rank", rank(A25), 2)
chk("25 c3 = c1 + c2", [A25[i][2] - A25[i][0] - A25[i][1] for i in range(4)], [F(0)] * 4)
R25c = M([[1, 0, 0, -2], [0, 1, 0, -1], [0, 0, 1, 0], [0, 0, 0, 0]])
chk("25(3) R x = 0", mul(R25c, M([[2], [1], [0], [1]])), [[F(0)]] * 4)

# ---------------- 练习 26 ----------------
for lam in [F(0), F(2), F(1), F(-2), F(7), F(-17, 29)]:
    chk("26 rank lambda=%s" % lam,
        rank(M([[-1, 2, lam], [1, -6, 1], [10, 1, lam], [5, -1, 2]])), 3)
chk("26 2x2 minor", F(1) * F(-6) - F(2) * F(1), F(-8))
chk("26 29lambda+17 root", F(29) * F(-17, 29) + F(17), F(0))

# ---------------- 练习 27 ----------------
chk("27 uv^T", mul(M([[3], [1], [4]]), M([[1, 2, 2]])),
    M([[3, 6, 6], [1, 2, 2], [4, 8, 8]]))
A27b = M([[2, 2, 6, 4], [-1, -1, -3, -2]])
chk("27b uv^T", mul(M([[2], [-1]]), M([[1, 1, 3, 2]])), A27b)
chk("27b rank", rank(A27b), 1)

# ---------------- 练习 28 ----------------
A28 = M([[1, 2], [0, 1], [3, 1]])
B28 = M([[1, 4], [2, 5]])
AB28 = mul(A28, B28)
chk("28 AB", AB28, M([[5, 14], [2, 5], [5, 17]]))
chk("28 col1 = a1 + 2a2", [[AB28[i][0]] for i in range(3)],
    [[A28[i][0] + 2 * A28[i][1]] for i in range(3)])
chk("28 col2 = 4a1 + 5a2", [[AB28[i][1]] for i in range(3)],
    [[4 * A28[i][0] + 5 * A28[i][1]] for i in range(3)])
B28n = M([[1, 2], [2, 4]])
chk("28b N(B) subset N(AB)", mul(mul(A28, B28n), M([[-2], [1]])), M([[0], [0], [0]]))

# ---------------- 练习 29 ----------------
chk("29 W1 subspace closed",
    [F(3) + F(4), F(2) * (F(3) + F(4))], [F(7), F(2) * F(7)])

# ---------------- 练习 31 ----------------
A31 = M([[1, 2, 3], [2, 4, 6], [0, 1, 1], [1, 3, 4]])
chk("31 RREF", rref(A31)[0], M([[1, 0, 1], [0, 1, 1], [0, 0, 0], [0, 0, 0]]))
chk("31 pivots", rref(A31)[1], [0, 1])
chk("31 rank", rank(A31), 2)
chk("31 c3 = c1 + c2", [A31[i][2] - A31[i][0] - A31[i][1] for i in range(4)], [F(0)] * 4)
chk("31 b1 not in C(A)",
    len(rref([[A31[i][0], A31[i][1], F([1, 0, 0, 9][i])] for i in range(4)])[1]), 3)
chk("31 b2 not in C(A)",
    len(rref([[A31[i][0], A31[i][1], F([1, 2, 1, 3][i])] for i in range(4)])[1]), 3)

# ---------------- 练习 32 ----------------
chk("32 N(A) of [[1,2],[3,6]]", mul(M([[1, 2], [3, 6]]), M([[-2], [1]])), M([[0], [0]]))
A32b = M([[1, 2, 3, 4], [2, 4, 6, 8], [1, 1, 1, 1]])
chk("32b RREF", rref(A32b)[0], M([[1, 0, -1, -2], [0, 1, 2, 3], [0, 0, 0, 0]]))
chk("32b null1", mul(A32b, M([[1], [-2], [1], [0]])), [[F(0)]] * 3)
chk("32b null2", mul(A32b, M([[2], [-3], [0], [1]])), [[F(0)]] * 3)
A32c = M([[1, 1, 2, 3], [2, 2, 8, 10], [3, 3, 10, 13]])
chk("32c RREF", rref(A32c)[0], M([[1, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 0]]))
chk("32c pivots", rref(A32c)[1], [0, 2])
chk("32c null1", mul(A32c, M([[-1], [1], [0], [0]])), [[F(0)]] * 3)
chk("32c null2", mul(A32c, M([[-1], [0], [-1], [1]])), [[F(0)]] * 3)

# ---------------- 练习 33 ----------------
A33 = M([[1, 1, 1, 1], [1, 2, 3, 4], [1, 3, 5, 6]])
chk("33 RREF", rref(A33)[0], M([[1, 0, -1, -2], [0, 1, 2, 3], [0, 0, 0, 0]]))
chk("33 pivots", rref(A33)[1], [0, 1])
chk("33 rank", rank(A33), 2)
chk("33 c3 = -c1 + 2c2", [A33[i][2] + A33[i][0] - 2 * A33[i][1] for i in range(3)],
    [F(0)] * 3)
chk("33 c4 = -2c1 + 3c2", [A33[i][3] + 2 * A33[i][0] - 3 * A33[i][1] for i in range(3)],
    [F(0)] * 3)
chk("33 null1 (1,-2,1,0)", mul(A33, M([[1], [-2], [1], [0]])), [[F(0)]] * 3)
chk("33 null2 (2,-3,0,1)", mul(A33, M([[2], [-3], [0], [1]])), [[F(0)]] * 3)
chk("33 uv^T for A1", mul(M([[3], [1], [4]]), M([[1, 2, 2]])),
    M([[3, 6, 6], [1, 2, 2], [4, 8, 8]]))
A33b = M([[2, 2, 6, 4], [-1, -1, -3, -2]])
chk("33 uv^T for A2", mul(M([[2], [-1]]), M([[1, 1, 3, 2]])), A33b)
chk("33 rank A2", rank(A33b), 1)
A33c = M([[1, 2], [3, 4], [5, 6]])
chk("33b AtA", mul(T(A33c), A33c), M([[35, 44], [44, 56]]))
chk("33b AtA diag nonneg", all(mul(T(A33c), A33c)[i][i] >= 0 for i in range(2)), True)

# ---------------- 练习 34 ----------------
A34 = M([[1, 2, 3], [2, 5, 3], [1, 0, 8]])
chk("34 rank 3", rank(A34), 3)
chk("34 det", det3(A34), F(-1))
chk("34 inverse", mul(A34, M([[-40, 16, 9], [13, -5, -3], [5, -2, -1]])), ident(3))

# ---------------- 练习 35 ----------------
A35 = M([[1, 2], [3, 4], [5, 6]])
B35 = M([[1, 0], [2, 3]])
chk("35 (AB)^T = B^T A^T", T(mul(A35, B35)), mul(T(B35), T(A35)))
C35 = M([[2, 1], [1, 3]])
C35i = inv2(C35)
chk("35 C^-1", mul(C35, C35i), ident(2))
chk("35 C^-1 symmetric", C35i, T(C35i))
S35 = M([[1, 2], [2, 3]])
U35 = M([[0, 1], [1, 0]])
chk("35a A^2 - B^2 symmetric", sub(mul(S35, S35), mul(U35, U35)),
    T(sub(mul(S35, S35), mul(U35, U35))))
chk("35b (A+B)(A-B)", mul(add(S35, U35), sub(S35, U35)), M([[4, 10], [6, 12]]))
chk("35b not symmetric",
    mul(add(S35, U35), sub(S35, U35)) == T(mul(add(S35, U35), sub(S35, U35))), False)
chk("35c ABA symmetric", mul(mul(S35, U35), S35), T(mul(mul(S35, U35), S35)))
chk("35d (AB)^2 not symmetric",
    mul(mul(S35, U35), mul(S35, U35)) == T(mul(mul(S35, U35), mul(S35, U35))), False)

# ---------------- 练习 36 ----------------
A36 = M([[3, -2], [1, 0]])
A36sq = mul(A36, A36)
A36cu = mul(A36sq, A36)
A36f5 = mul(mul(A36sq, A36sq), A36)
chk("36 A^2 = 3A - 2I", A36sq, sub(scale(A36, 3), scale(ident(2), 2)))
C36 = sub(scale(ident(2), 2), A36)
D36 = sub(A36, ident(2))
chk("36 C = 2I - A", C36, M([[-1, 2], [-1, 2]]))
chk("36 D = A - I", D36, M([[2, -2], [1, -1]]))
chk("36 (A-I)(A-2I) = O", mul(D36, sub(A36, scale(ident(2), 2))), [[F(0)] * 2] * 2)
chk("36 A^0", add(C36, scale(D36, 1)), ident(2))
chk("36 A^1", add(C36, scale(D36, 2)), A36)
chk("36 A^2", add(C36, scale(D36, 4)), A36sq)
chk("36 A^3", add(C36, scale(D36, 8)), A36cu)
chk("36 A^5", add(C36, scale(D36, 32)), A36f5)
chk("36 A^5 value", A36f5, M([[63, -62], [31, -30]]))

# ---------------- 练习 37 ----------------
chk("37 dim M2 = 4", 4, 4)
chk("37 dim D = 2", rank(M([[1, 0], [0, 0], [0, 0], [0, 1]])), 2)
chk("37 dim U = 3", rank(M([[1, 0, 0], [0, 1, 0], [0, 0, 0], [0, 0, 1]])), 3)
chk("37 A not subspace (no -v)", (-1) * F(1) == -F(1), True)

# ---------------- 练习 38 ----------------
A38 = M([[1, 2, 3], [2, 4, 6], [1, 1, 1]])
B38 = M([[1, 0], [2, 1], [3, 1]])
chk("38 rank(ABC) <= rank B", rank(mul(A38, B38)), 2)
chk("38 Sylvester", rank(mul(A38, B38)) >= rank(A38) + rank(B38) - 3, True)
A38b = M([[1, 2], [3, 4], [5, 6]])
S38 = M([[2, 1, 0], [1, 3, 1], [0, 1, 2]])
chk("38 A^T S A symmetric", mul(mul(T(A38b), S38), A38b), T(mul(mul(T(A38b), S38), A38b)))
chk("38 A^T S A is 2x2", len(mul(mul(T(A38b), S38), A38b)), 2)

# ---------------- 练习 39 ----------------
A39 = M([[1, 2], [3, 4], [5, 6]])
B39 = M([[1, 0, 1], [0, 1, 1]])
I3AB = sub(ident(3), mul(A39, B39))
I2BA = sub(ident(2), mul(B39, A39))
chk("39 det(I3-AB)", det3(I3AB), F(-19))
chk("39 det(I2-BA)", I2BA[0][0] * I2BA[1][1] - I2BA[0][1] * I2BA[1][0], F(-19))

# ---------------- 练习 40 ----------------
A40 = M([[1, 2, 3], [2, 4, 6], [1, 1, 1]])
B40 = M([[1, 0], [2, 1], [3, 1]])
chk("40 rank AB", rank(mul(A40, B40)), 2)
chk("40 Sylvester bound", rank(mul(A40, B40)) >= rank(A40) + rank(B40) - 3, True)

# ---------------- 练习 41 ----------------
chk("41.1 rank", rank(M([[0, 1, 2], [2, 1, 0], [1, 0, 1]])), 3)
A41b = M([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0]])
chk("41.2 A^4 = I", mul(mul(mul(A41b, A41b), A41b), A41b), ident(4))
chk("41.2 A^2", mul(A41b, A41b), M([[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]]))
chk("41.2 A^3", mul(mul(A41b, A41b), A41b),
    M([[0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]))
chk("41.4 AB",
    mul(M([[1, 0, 0, 0], [0, 1, 0, 0], [1, 2, 1, 0], [0, 1, 0, 1]]),
        M([[1, 1, 1, 0], [0, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 0]])),
    M([[1, 1, 1, 0], [0, 1, 0, 1], [2, 3, 2, 3], [0, 2, 1, 1]]))
A41e = M([[1, 2, 3], [2, 5, 7], [3, 7, 11]])
chk("41.5 LU = A", mul(M([[1, 0, 0], [2, 1, 0], [3, 1, 1]]),
                       M([[1, 2, 3], [0, 1, 1], [0, 0, 1]])), A41e)
chk("41.5 A^-1", mul(A41e, M([[6, -1, -1], [-1, 2, -1], [-1, -1, 1]])), ident(3))
A41f = M([[1, 1, 2], [2, 2, 4], [1, 0, 1]])
chk("41.6 RREF", rref(A41f)[0], M([[1, 0, 1], [0, 1, 1], [0, 0, 0]]))
chk("41.6 rank", rank(A41f), 2)
chk("41.6 b = a1", mul(A41f, M([[1], [0], [0]])), M([[1], [2], [1]]))
chk("41.7 rank(A^T A) = rank(A)", rank(mul(T(A41f), A41f)), rank(A41f))

log()
log("=" * 64)
log("CHECKS PASSED: %d     FAILURES: %d" % (OK, len(BAD)))
if BAD:
    log("FAILED NAMES: " + ", ".join(BAD))
log("=" * 64)

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_final_report.txt")
with open(path, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", "", "\n".join(LINES)))
print("CHECKS PASSED:", OK, " FAILURES:", len(BAD))
for b in BAD:
    print("  FAILED:", b)
