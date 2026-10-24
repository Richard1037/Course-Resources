"""Canonical computations for exercise_dpsk.md. Prints every value used in the text."""
from fractions import Fraction as F


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
    return len(rref(A)[1])


def txt(X):
    """Render a matrix as a compact bracket string."""
    if not isinstance(X, list):
        return str(X)
    if X and not isinstance(X[0], list):
        return "[" + ", ".join(str(x) for x in X) + "]"
    return "[" + " ; ".join(", ".join(str(x) for x in r) for r in X) + "]"


def P(name, X):
    print("%-34s %s" % (name, txt(X) if isinstance(X, list) else X))


def check(name, got, want):
    ok = got == want
    print("%-34s %s" % (name, "OK" if ok else "MISMATCH got=%s want=%s" % (got, want)))


print("=" * 78)
print("E1  A = [[2,-1,0],[1,3,-2],[-1,0,4]]")
A1 = M([[2, -1, 0], [1, 3, -2], [-1, 0, 4]])
P("rank A1", rank(A1))
eq = lambda name, g, w: check(name, g, w)
P("2A1 - I3", sub(scale(A1, 2), ident(3)))

print()
print("E2  A = 2 * cyclic4")
A2 = M([[0, 2, 0, 0], [0, 0, 2, 0], [0, 0, 0, 2], [2, 0, 0, 0]])
P("A^2", mul(A2, A2))
P("A^3", mul(mul(A2, A2), A2))
P("A^4", mul(mul(mul(A2, A2), A2), A2))

print()
print("E3  B = 3 * cyclic4 ; N nilpotent")
B3 = M([[0, 3, 0, 0], [0, 0, 3, 0], [0, 0, 0, 3], [3, 0, 0, 0]])
P("B^2", mul(B3, B3))
P("B^3", mul(mul(B3, B3), B3))
P("B^4", mul(mul(mul(B3, B3), B3), B3))
N3 = M([[0, 5, 0, 0], [0, 0, 5, 0], [0, 0, 0, 5], [0, 0, 0, 0]])
P("N^2", mul(N3, N3))
P("N^3", mul(mul(N3, N3), N3))
P("N^4", mul(mul(mul(N3, N3), N3), N3))

print()
print("E4  block product (exam Q4 with A1 = [[2,-1],[-3,1]])")
A4 = M([[1, 0, 0, 0], [0, 1, 0, 0], [2, -1, 1, 0], [-3, 1, 0, 1]])
B4 = M([[1, 0, 3, 2], [-1, 2, 0, 1], [1, 0, 4, 1], [-1, -1, 2, 0]])
P("A4 B4", mul(A4, B4))

print()
print("E5  LDU (exam Q5 with A = [[2,1,1],[4,3,3],[8,7,9]])")
A5 = M([[2, 1, 1], [4, 3, 3], [8, 7, 9]])
L5 = M([[1, 0, 0], [2, 1, 0], [4, 3, 1]])
D5 = M([[2, 0, 0], [0, 1, 0], [0, 0, 2]])
U5 = M([[1, F(1, 2), F(1, 2)], [0, 1, 1], [0, 0, 1]])
P("L D U", mul(mul(L5, D5), U5))
P("check = A5", mul(mul(L5, D5), U5) == A5)
P("L^-1", M([[1, 0, 0], [-2, 1, 0], [2, -3, 1]]))
P("D^-1", M([[F(1, 2), 0, 0], [0, 1, 0], [0, 0, F(1, 2)]]))
P("U^-1", M([[1, F(-1, 2), 0], [0, 1, -1], [0, 0, 1]]))
P("A5^-1", mul(mul(M([[1, F(-1, 2), 0], [0, 1, -1], [0, 0, 1]]),
                   M([[F(1, 2), 0, 0], [0, 1, 0], [0, 0, F(1, 2)]])),
               M([[1, 0, 0], [-2, 1, 0], [2, -3, 1]])))

print()
print("E6  rank-3 4x4 (exam Q6 analogue)")
A6 = M([[1, 0, 0, 4],
        [0, 1, 0, 4],
        [0, 0, 1, 3],
        [-1, -2, 1, -9]])
R6, piv6 = rref(A6)
P("A6", A6)
P("RREF", R6)
P("pivots", piv6)
P("rank", rank(A6))
P("null basis", M([[-4], [-4], [-3], [1]]))
P("A6 * null", mul(A6, M([[-4], [-4], [-3], [1]])))
P("left null y", M([[1], [2], [-1], [1]]))
P("y^T A6", mul(M([[1, 2, -1, 1]]), A6))
for bb in ([1, 1, 2, -1], [0, 0, 0, 0], [2, -1, 3, -3]):
    b = M([[v] for v in bb])
    xp = M([[F(bb[0])], [F(bb[1])], [F(bb[2])], [F(0)]])
    P("b=%s -> xp" % (bb,), mul(A6, xp))
    P("   residual equals b?", mul(A6, xp) == b)
P("b=(1,2,3,4) y.b", 1 * 1 + 2 * 2 - 1 * 3 + 1 * 4)

print()
print("E7  rank inequalities")
A7 = M([[1, 2, 3], [2, 4, 6], [1, 1, 1]])
B7 = M([[1, 0], [2, 1], [3, 1]])
P("rankA7", rank(A7))
P("rankB7", rank(B7))
P("A7 B7", mul(A7, B7))
P("rank A7B7", rank(mul(A7, B7)))

print()
print("E8  block inverse + I-AB")
Bc = M([[1, 2], [3, 4]])
Cc = M([[2, 1], [1, 1]])
Cinv = M([[1, -1], [-1, 2]])
Z2 = [[F(0)] * 2 for _ in range(2)]
Blk = [[ident(2), Z2], [Bc, Cc]]
TrueInv = [[ident(2), Z2], [scale(mul(Cinv, Bc), -1), Cinv]]
flat = lambda blocks: [sum(([x for x in blk[i]] for blk in brow), [])
                       for brow in blocks for i in range(len(brow[0]))]
P("block S", flat(Blk))
P("S^-1", flat(TrueInv))
P("S S^-1", mul(flat(Blk), flat(TrueInv)))
Am = M([[2, 1], [1, 1]])
Dm = M([[1, 0], [0, 3]])
P("I2 - Am Dm", sub(ident(2), mul(Am, Dm)))
MABi = M([[F(-2), F(3)], [F(1), F(-1)]])
P("(I2-AmDm)^-1", MABi)
P("check", mul(sub(ident(2), mul(Am, Dm)), MABi))
P("I2 - Dm Am", sub(ident(2), mul(Dm, Am)))
P("(I2-DmAm)^-1", add(ident(2), mul(mul(Dm, MABi), Am)))
P("BA identity", mul(sub(ident(2), mul(Dm, Am)),
                      add(ident(2), mul(mul(Dm, MABi), Am))))

print()
print("E9  dependence")
P9 = M([[1, 2, 2, 5], [2, -1, 4, 5], [3, 1, 6, 10], [1, 0, 2, 3]])
P("rank P9", rank(P9))
c1 = [P9[i][0] for i in range(4)]
c2 = [P9[i][1] for i in range(4)]
c3 = [P9[i][2] for i in range(4)]
c4 = [P9[i][3] for i in range(4)]
P("c3 - 2c1", [c3[i] - 2 * c1[i] for i in range(4)])
P("c4 - 3c1 - c2", [c4[i] - 3 * c1[i] - c2[i] for i in range(4)])

print()
print("E10  AB != BA , trace")
X10 = M([[1, 2], [0, 0]])
Y10 = M([[0, 0], [3, 4]])
P("XY", mul(X10, Y10))
P("YX", mul(Y10, X10))
B10 = M([[1, 2, 3], [4, 5, 6]])
C10 = M([[1, 2], [3, 4], [5, 6]])
P("BC", mul(B10, C10))
P("CB", mul(C10, B10))
P("tr BC", sum(mul(B10, C10)[i][i] for i in range(2)))
P("tr CB", sum(mul(C10, B10)[i][i] for i in range(3)))
R10 = M([[-1, 1, 0], [0, -1, 1]])
P("R^T R", mul(T(R10), R10))
P("R R^T", mul(R10, T(R10)))

print()
print("E11  zero pivot elimination (y+z=2 ; x+y+z=3 ; x+2y+3z=6)")
A11 = M([[0, 1, 1], [1, 1, 1], [1, 2, 3]])
P("A11", A11)
P("swap A11", mul(M([[0, 1, 0], [1, 0, 0], [0, 0, 1]]), A11))
b11 = M([[2], [3], [6]])
P("x=(1,1,1)", mul(A11, M([[1], [1], [1]])))

print()
print("E12  parameter system (x+4y-2z=1 ; x+7y-6z=6 ; 3y+qz=t)")
for q, t in [(0, 0), (-3, 0), (5, 0)]:
    Aug = M([[1, 4, -2, 1], [1, 7, -6, 6], [0, 3, q, t]])
    R, p = rref(Aug)
    P("q=%s t=%s rankA" % (q, t), rank(M([[1, 4, -2], [1, 7, -6], [0, 3, q]])))
    P("   RREF", R)
    P("   pivots", p)
# general solution at q=-3 : z=s, y=(5+4s)/3, x=(-17-10s)/3, t = 3y - 3z
for s in [F(0), F(1), F(-2)]:
    y = (5 + 4 * s) / 3
    x = (-17 - 10 * s) / 3
    P("q=-3 s=%s (x,y,z)" % s, [x, y, s])
    P("   eq1", x + 4 * y - 2 * s)
    P("   eq2", x + 7 * y - 6 * s)
    P("   t   ", 3 * y - 3 * s)

print()
print("E13  linear combination")
A13 = M([[2, -5, -3], [-5, 11, 7], [3, 3, -1], [-4, 10, 6]])
b13 = M([[13], [-30], [2], [-26]])
P("coef (2,3,-2)", mul(A13, M([[2], [3], [-2]])))

print()
print("E14  C(A)=C(B)")
A14 = M([[1, 2], [2, 4], [3, 6]])
b14 = M([[2], [4], [6]])
P("rank A14", rank(A14))
P("rank [A|b]", rank([[A14[i][0], A14[i][1], b14[i][0]] for i in range(3)]))

print()
print("E15  Gauss-Jordan inverse of [[1,2,3],[2,5,3],[1,0,8]]")
A15 = M([[1, 2, 3], [2, 5, 3], [1, 0, 8]])
A15i = M([[-40, 16, 9], [13, -5, -3], [5, -2, -1]])
P("A15 A15i", mul(A15, A15i))

print()
print("E16  elementary matrices")
E16 = M([[1, 0, 0], [3, 1, 0], [0, 0, 1]])
P16 = M([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
Mm = M([[1, -2], [3, 1], [0, 4]])
P("P E M", mul(mul(P16, E16), Mm))
P("(P E)^-1", mul(M([[1, 0, 0], [-3, 1, 0], [0, 0, 1]]), P16))

print()
print("E17  invertibility checks")
P("diag(1,2,3)^-1", M([[1, 0, 0], [0, F(1, 2), 0], [0, 0, F(1, 3)]]))
B17 = M([[2, 1, 1], [1, 2, 1], [1, 1, 2]])
B17i = M([[F(3, 4), F(-1, 4), F(-1, 4)], [F(-1, 4), F(3, 4), F(-1, 4)], [F(-1, 4), F(-1, 4), F(3, 4)]])
P("B17 B17i", mul(B17, B17i))
C17 = M([[2, -1, -1], [-1, 2, -1], [-1, -1, 2]])
P("C17 rank", rank(C17))
P("C17 (1,1,1)", mul(C17, M([[1], [1], [1]])))
D17 = M([[0, 0, 0, 2], [0, 0, 3, 0], [0, 4, 0, 0], [5, 0, 0, 0]])
D17i = M([[0, 0, 0, F(1, 5)], [0, 0, F(1, 4), 0], [0, F(1, 3), 0, 0], [F(1, 2), 0, 0, 0]])
P("D17 D17i", mul(D17, D17i))
L17 = M([[1, 0, 0], [1, 1, 0], [1, 1, 1]])
P("L17^-1", M([[1, 0, 0], [-1, 1, 0], [0, -1, 1]]))
P("check", mul(L17, M([[1, 0, 0], [-1, 1, 0], [0, -1, 1]])))

print()
print("E18  LU of [[1,0,1],[2,2,2],[3,4,5]]")
A18 = M([[1, 0, 1], [2, 2, 2], [3, 4, 5]])
L18 = M([[1, 0, 0], [2, 1, 0], [3, 2, 1]])
U18 = M([[1, 0, 1], [0, 2, 0], [0, 0, 2]])
P("L18 U18", mul(L18, U18))
P("equals A18", mul(L18, U18) == A18)
P("det", U18[0][0] * U18[1][1] * U18[2][2])

print()
print("E19  LU solve, two right-hand sides")
A19 = M([[1, 1, 1], [1, 2, 2], [1, 2, 3]])
L19 = M([[1, 0, 0], [1, 1, 0], [1, 1, 1]])
U19 = M([[1, 1, 1], [0, 1, 1], [0, 0, 1]])
P("L19 U19", mul(L19, U19))
for bb, xw in [([3, 5, 6], [F(1), F(1), F(1)]), ([4, 5, 6], [F(3), F(0), F(1)])]:
    P("b=%s x" % (bb,), xw)
    P("   residual", mul(A19, [[v] for v in xw]))

print()
print("E20  LDL^T")
L20 = M([[1, 0, 0], [F(-1, 2), 1, 0], [0, F(-2, 3), 1]])
D20 = M([[2, 0, 0], [0, F(3, 2), 0], [0, 0, F(4, 3)]])
P("L D L^T", mul(mul(L20, D20), T(L20)))
L20b = M([[1, 0, 0], [2, 1, 0], [2, 1, 1]])
D20b = M([[1, 0, 0], [0, 3, 0], [0, 0, F(-1, 3)]])
P("Lb Db Lb^T", mul(mul(L20b, D20b), T(L20b)))
P("logical", [F(1) * 3 * F(-1, 3)])

print()
print("E21  permutation matrices")
P21 = M([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
Q21 = M([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
P("P21 Q21", mul(P21, Q21))
P("P21^-1 = P21^T", mul(P21, T(P21)))

print()
print("E22  PA = LU  (A = [[2,1,0],[1,2,2],[1,3,0]])")
A22 = M([[2, 1, 0], [1, 2, 2], [1, 3, 0]])
P22 = M([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
PA22 = mul(P22, A22)
P("P22 A22", PA22)
E1 = M([[1, 0, 0], [-F(1, 2), 1, 0], [0, 0, 1]])
t1 = mul(E1, PA22)
P("after E1", t1)
E2 = M([[1, 0, 0], [0, 1, 0], [-1, 0, 1]])
t2 = mul(E2, t1)
P("after E2", t2)
E3 = M([[1, 0, 0], [0, 1, 0], [0, F(1, 3), 1]])
t3 = mul(E3, t2)
P("after E3 (=U)", t3)
L22 = M([[1, 0, 0], [F(1, 2), 1, 0], [1, -F(1, 3), 1]])
P("L22", L22)
P("L22 U22", mul(L22, t3))
P("equals P22 A22", mul(L22, t3) == PA22)

print()
print("E23  Schur complement")
A23 = M([[2, 1], [1, 2]])
C23 = M([[3, 1], [2, 1]])
B23 = M([[3, 2], [1, 1]])
D23 = M([[16, 9], [9, 23]])
A23i = M([[F(2, 3), F(-1, 3)], [F(-1, 3), F(2, 3)]])
P("A23^-1", A23i)
P("check", mul(A23, A23i))
CAiB = mul(mul(C23, A23i), B23)
P("C A^-1 B", CAiB)
P("S = D - C A^-1 B", sub(D23, CAiB))
S23 = sub(D23, CAiB)
P("det S", S23[0][0] * S23[1][1] - S23[0][1] * S23[1][0])
P("-C A^-1", scale(mul(A23i, C23), -1))
Sfull = M([[2, 1, 3, 2], [1, 2, 1, 1], [3, 1, 16, 9], [2, 1, 9, 23]])
Eblk = [[ident(2), Z2], [scale(mul(A23i, C23), -1), ident(2)]]
P("E S", mul(flat(Eblk), Sfull))

print()
print("E24  nullspace of 4x3")
A24 = M([[0, 1, 1], [0, 2, 5], [0, 0, 1], [0, 1, 1]])
R24, p24 = rref(A24)
P("RREF", R24)
P("pivots", p24)
P("rank", rank(A24))
P("null basis (1,0,0)", mul(A24, M([[1], [0], [0]])))

print()
print("E25  RREF preserves relations")
A25 = M([[1, 1, 2], [1, 2, 3], [1, 2, 3], [1, 3, 4]])
R25, p25 = rref(A25)
P("RREF", R25)
P("pivots", p25)
P("rank", rank(A25))
P("c3 - c1 - c2", [A25[i][2] - A25[i][0] - A25[i][1] for i in range(4)])

print()
print("E26  rank depends on lambda (third row = row1 + row2 at lambda = 1)")
A26 = M([[-1, 2, 1], [1, -6, 1], [10, 1, 1], [5, -1, 2]])
P("rank lambda=1", rank(A26))
P("row1+row2-row3", [A26[0][j] + A26[1][j] - A26[2][j] for j in range(3)])
P("rank lambda=0", rank(M([[-1, 2, 0], [1, -6, 1], [10, 1, 0], [5, -1, 2]])))
P("rank lambda=2", rank(M([[-1, 2, 2], [1, -6, 1], [10, 1, 2], [5, -1, 2]])))

print()
print("E27  rank-1 matrices")
P("uvT", mul(M([[3], [1], [4]]), M([[1, 2, 2]])))
A27b = M([[2, 2, 6, 4], [-1, -1, -3, -2]])
P("A27b", A27b)
P("rank A27b", rank(A27b))

print()
print("E28  columns of AB are combinations of columns of A")
A28 = M([[1, 2], [0, 1], [3, 1]])
B28 = M([[1, 4], [2, 5]])
P("A28 B28", mul(A28, B28))

print()
print("E29  I - AB")
Ac = M([[1, 2], [3, 4], [5, 6]])
Bc2 = M([[1, 0, 1], [0, 1, 1]])
MAB = sub(ident(3), mul(Ac, Bc2))
P("I3 - AB", MAB)
MBA = sub(ident(2), mul(Bc2, Ac))
P("I2 - BA", MBA)
P("det(I2-BA)", MBA[0][0] * MBA[1][1] - MBA[0][1] * MBA[1][0])
MBAi = M([[F(7, 19), F(10, 19)], [F(-2, 19), F(-5, 19)]])
P("(I2-BA)^-1", MBAi)
P("check", mul(MBA, MBAi))
P("identity", mul(MAB, add(ident(3), mul(mul(Ac, MBAi), Bc2))))

print()
print("E30  transpose / symmetric")
A30 = M([[1, 2], [3, 4], [5, 6]])
B30 = M([[1, 0], [2, 3]])
P("(AB)^T", T(mul(A30, B30)))
P("B^T A^T", mul(T(B30), T(A30)))
P("A^T A", mul(T(A30), A30))
C30 = M([[2, 1], [1, 3]])
C30i = M([[F(3, 5), F(-1, 5)], [F(-1, 5), F(2, 5)]])
P("C30^-1", C30i)
P("(C^-1)^T", T(C30i))

print()
print("E31  symmetric T/F")
S31 = M([[1, 2], [2, 3]])
U31 = M([[0, 1], [1, 0]])
P("S^2 - U^2", sub(mul(S31, S31), mul(U31, U31)))
P("(S+U)(S-U)", mul(add(S31, U31), sub(S31, U31)))
P("SU - US", sub(mul(S31, U31), mul(U31, S31)))
P("SUS", mul(mul(S31, U31), S31))
P("(SU)^2", mul(mul(S31, U31), mul(S31, U31)))
print()
print("E32  A^n recurrence for A = [[3,-2],[1,0]]")
A32 = M([[3, -2], [1, 0]])
P("A^2", mul(A32, A32))
P("3A - 2I", sub(scale(A32, 3), scale(ident(2), 2)))
C32 = sub(scale(ident(2), 2), A32)
D32 = sub(A32, ident(2))
P("C = 2I - A", C32)
P("D = A - I", D32)
P("C + D", add(C32, D32))
for n in [0, 1, 2, 3, 5]:
    P("A^%d (formula)" % n, add(C32, scale(D32, 2 ** n)))
P("A^5 (powers)", mul(mul(mul(mul(A32, A32), A32), A32), A32))

print()
print("E33  subspace dimensions")
U33 = M([[1, 0, 4], [2, 1, 5], [0, 0, 1]])
P("rank U33", rank(U33))
V33 = M([[1, 8, 6], [0, 0, 0], [0, 0, 0]])
P("rank V33", rank(V33))
print("dim D (diagonal 2x2) = 2 ; dim U (upper triangular 2x2) = 3")

print()
print("=" * 78)
print("done")
