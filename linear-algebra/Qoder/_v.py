from _mx import M, mm, mv, det, rref, inv, eye, p

def show(t, A):
    print(t, *[r for r in p(A)], sep='\n   ')

def hblock(TL,TR,BL,BR):
    n=len(TL); m=len(BL)
    return [[*TL[i],*TR[i]] for i in range(n)] + [[*BL[i],*BR[i]] for i in range(m)]

# ---- Q25: A=[[0,2,1],[1,1,1],[2,1,2]], P12 A = LU, solve Ax=(1,1,2)
A = M((0,2,1),(1,1,1),(2,1,2))
Pl = M((0,1,0),(1,0,0),(0,0,1))
L = M((1,0,0),(0,1,0),("2","-1/2",1))
U = M((1,1,1),(0,2,1),(0,0,"1/2"))
print("PA == LU ?", p(mm(Pl, A)) == p(mm(L, U)))
print("det A", det(A), " det U", det(U), " det P", det(Pl))
b = [1,1,2]
print("Pb =", mv(Pl, b))
pb = mv(Pl, b); y = []
for i in range(3):
    y.append(pb[i] - sum(L[i][k]*y[k] for k in range(i)))
print("Ly=Pb -> y =", [str(v) for v in y])
z = [None]*3
for i in range(2,-1,-1):
    z[i] = (y[i] - sum(U[i][k]*z[k] for k in range(i+1,3)))/U[i][i]
print("Ux=y  -> x =", [str(v) for v in z], " Ax =", mv(A, z))
show("A^-1", inv(A))

# ---- Q14(3): A = [[I,O],[-A1,I]]
A1 = M((2,-1),(1,3))
I2 = eye(2); O = M((0,0),(0,0))
Avar = hblock(I2, O, [[-x for x in r] for r in A1], I2)
show("A(var)", Avar)
B = M((1,0,0,3),(-1,2,1,-1),(5,-2,0,9),(-2,7,2,0))
show("B", B)
B11=M((1,0),(-1,2)); B12=M((0,3),(1,-1)); B21=M((5,-2),(-2,7)); B22=M((0,9),(2,0))
def add(X,Y): return [[X[i][j]+Y[i][j] for j in range(len(Y[0]))] for i in range(len(Y))]
show("A1*B11", mm(A1,B11)); show("A1B11+B21", add(mm(A1,B11),B21))
show("A1*B12", mm(A1,B12)); show("A1B12+B22", add(mm(A1,B12),B22))
show("AB(var)", mm(Avar,B))
# also original A = [[I,O],[A1,I]] for reference
Aorig = hblock(I2, O, A1, I2)
show("AB(orig)", mm(Aorig,B))

# ---- Q30(3): K=[[I_m,A],[A^T,O]]
A30 = M((1,0),(0,1),(1,1))            # 3x2 full column rank
AT = [list(col) for col in zip(*A30)]
ATA = mm(AT, A30); ATAi = inv(ATA)
show("A^T A", ATA); show("(A^TA)^-1", ATAi)
G = mm(A30, ATAi)                     # m x n
show("A(A^TA)^-1  (=G)", G)
top = [[(1 if i==j else 0) - sum(G[i][k]*AT[k][j] for k in range(2)) for j in range(3)] for i in range(3)]
show("I - G A^T", top)
K = hblock(eye(3), A30, AT, O)
show("K", K)
KI = hblock(top, G, [[x for x in r] for r in mm(ATAi, AT)], [[-x for x in r] for r in ATAi])
show("K^-1", KI)
print("K*K^-1 == I5 ?", p(mm(K,KI)) == p(eye(5)), " K^-1*K == I5 ?", p(mm(KI,K)) == p(eye(5)))
print("det K =", det(K), " det(-A^TA) =", det([[-x for x in r] for r in ATA]))
show("K*K^-1", mm(K,KI))

# ---- Q9(4): AB != BA examples
for (X, Y, tag) in [(M((1,0),(0,0)), M((1,1),(1,1)), "E11 * J"),
                    (M((0,1),(0,0)), M((1,0),(0,0)), "E12*E11"),
                    (M((1,2),(3,4)), M((0,1),(0,0)), "A*E12")]:
    show(tag+" : AB", mm(X,Y)); show(tag+" : BA", mm(Y,X))
