from fractions import Fraction as F


def M(rows):
    return [[F(x) for x in r] for r in rows]


def mul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]


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


print("--- ex2 ---")
C4 = M([[0, 2, 0, 0], [0, 0, 2, 0], [0, 0, 0, 2], [2, 0, 0, 0]])
C2 = mul(C4, C4)
C3 = mul(C2, C4)
C4p = mul(C3, C4)
for nm, X in [("C4", C4), ("C2", C2), ("C3", C3), ("C4", C4p)]:
    print(nm, [[str(x) for x in r] for r in X])

print("--- ex4 ---")
Ab = M([[1, 0, 0, 0], [0, 1, 0, 0], [2, -1, 1, 0], [-3, 1, 0, 1]])
Bb = M([[1, 0, 3, 2], [-1, 2, 0, 1], [1, 0, 4, 1], [-1, -1, 2, 0]])
print("direct", [[str(x) for x in r] for r in mul(Ab, Bb)])
A1 = M([[2, -1], [-3, 1]])
B11 = M([[1, 0], [-1, 2]])
B12 = M([[3, 2], [0, 1]])
B21 = M([[1, 0], [-1, -1]])
B22 = M([[4, 1], [2, 0]])
A1B11 = mul(A1, B11)
A1B12 = mul(A1, B12)
print("A1B11", [[str(x) for x in r] for r in A1B11])
print("A1B12", [[str(x) for x in r] for r in A1B12])
print("BL", [[str(a + b) for a, b in zip(r1, r2)] for r1, r2 in zip(A1B11, B21)])
print("BR", [[str(a + b) for a, b in zip(r1, r2)] for r1, r2 in zip(A1B12, B22)])

print("--- ex6 ---")
A6 = M([[0, 3, -2, 4, 1], [0, 0, 5, -3, 6], [7, 0, 0, 8, 4], [7, 3, 3, 9, 3]])
R, p = rref(A6)
print("rank", len(p), "pivots", p)
print("R", [[str(x) for x in r] for r in R])
xp = [F(0), F(0), F(0), F(1, 7), F(2, 7)]
print("A6 xp", [str(sum(A6[i][j] * xp[j] for j in range(5))) for i in range(4)])
