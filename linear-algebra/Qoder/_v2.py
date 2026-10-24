from _mx import M, mm, mv, det, rref, inv, eye, p

def show(t,A): print(t,*[r for r in p(A)],sep='\n   ')
def add(X,Y): return [[X[i][j]+Y[i][j] for j in range(len(Y[0]))] for i in range(len(Y))]

print("=== Q11")
A=M((2,-1,1),(0,3,-2),(1,0,4)); print("det A",det(A))
a1=[2,0,1]; a2=[-1,3,0]
nrm=lambda x:(x[0]**2+x[1]**2+x[2]**2)**0.5
cr=[a1[1]*a2[2]-a1[2]*a2[1], a1[2]*a2[0]-a1[0]*a2[2], a1[0]*a2[1]-a1[1]*a2[0]]
print("a1 x a2 =",[str(v) for v in cr])
a3=[1,-2,4]
print("n . a3 =", cr[0]*a3[0]+cr[1]*a3[1]+cr[2]*a3[2], " n.a1",sum(cr[i]*a1[i] for i in range(3))," n.a2",sum(cr[i]*a2[i] for i in range(3)))

print("=== Q12")
A=M((0,3,0,0),(0,0,3,0),(0,0,0,3),(3,0,0,0))
show("A2",mm(A,A)); show("A3",mm(mm(A,A),A)); show("A4",mm(mm(A,A),mm(A,A)))
show("A^-1 from A3/81", [[v/81 for v in r] for r in mm(mm(A,A),A)])
print("det A",det(A))

print("=== Q14  AB with A=[[I,O],[A1,I]]")
A1=M((2,-1),(1,3)); I2=eye(2); O=M((0,0),(0,0))
def hb(TL,TR,BL,BR): return [[*TL[i],*TR[i]] for i in range(len(TL))]+[[*BL[i],*BR[i]] for i in range(len(BL))]
A=hb(I2,O,A1,I2)
B=M((1,0,0,3),(-1,2,1,-1),(2,0,1,2),(0,1,-1,0))
show("A",A); show("AB",mm(A,B))

print("=== Q15 LDU")
A=M((1,1,2),(2,4,6),(1,7,11))
L=M((1,0,0),(2,1,0),(1,3,1)); D=M((1,0,0),(0,2,0),(0,0,3)); U=M((1,1,2),(0,1,1),(0,0,1))
print("LDU==A ?",p(mm(mm(L,D),U))==p(A))
show("L^-1",inv(L)); show("U^-1",inv(U)); show("A^-1",inv(A))
show("A^-1 b", [r for r in mm(inv(A),M((1),(2),(3)))])
Li=inv(L); Ui=inv(U)
show("E32(-3)E31(-1)E21(-2)", mm(M((1,0,0),(0,1,0),("0",-3,1)), mm(M((1,0,0),("0",1,0),("-3",0,1)),M((1,0,0),("-2",1,0),(0,0,1)))))

print("=== Q16")
A=M((1,2,0,-1,0),(2,4,1,1,0),(1,2,3,8,1),(0,0,1,3,2))
R,piv=rref([r[:] for r in A]); show("R",R); print("piv",piv,"det A",det(A))
# compatibility: y in N(A^T)
AT=[list(c) for c in zip(*A)]; NR,pvr=rref([r[:] for r in AT]); show("R(A^T)",NR)
y=M((-8),(5),(-2),(1)); print("A^T y =", mv(AT,[v[0] for v in y]))
b=M((2),(8),(15),(6)); print("y.b =", sum(y[i][0]*b[i][0] for i in range(4)))
# particular solution for b
Aug=[A[i]+[b[i][0]] for i in range(4)]; RA,pia=rref(Aug); show("R|b",RA)
# general: check xp=(2,0,4,0,1)
xp=[2,0,4,0,1]; print("A xp =", mv(A,xp))
nb1=[-2,1,0,0,0]; nb2=[1,0,-3,1,0]
print("A nb1",mv(A,nb1),"A nb2",mv(A,nb2))
# verify condition: for b general, solve consistency via rref of augmented symbolically not possible; check y basis count
print("dim N(A^T) pivots",pvr)

print("=== Q20")
A=M((1,2,1),(2,4,3),(1,3,2)); show("A^-1",inv(A)); print("x", mv(inv(A),[1,2,3]))

print("=== Q22")
L=M((1,0,0),(2,1,0),(1,3,1)); U=M((1,2,3),(0,2,3),(0,0,2))
# for A of Q15: plain LU
A=M((1,1,2),(2,4,6),(1,7,11))
LU=M((1,0,0),(2,1,0),(1,3,1)); UU=M((1,1,2),(0,2,2),(0,0,2))
print("LU==A?",p(mm(LU,UU))==p(A))
def solveLU(L,U,rhs):
    y=[];
    for i in range(3): y.append(rhs[i]-sum(L[i][k]*y[k] for k in range(i)))
    x=[None]*3
    for i in range(2,-1,-1): x[i]=(y[i]-sum(U[i][k]*x[k] for k in range(i+1,3)))/U[i][i]
    return x
print("b:",[str(v) for v in solveLU(LU,UU,[1,2,3])],"c:",[str(v) for v in solveLU(LU,UU,[0,1,1])])
print("check A x_c", mv(A, solveLU(LU,UU,[0,1,1])))

print("=== Q23 2x2 LDU")
a,b_,d=2,1,2
L=M((1,0),(str(b_),"1"),(0,0)) if False else M((1,0),("1",1))
# general: pivots a, d-b^2/a ; L=[[1,0],[b/a,1]], D=diag(a,(ad-b^2)/a), U=[[1,b/a],[0,1]]
Lg=M((1,0),(str(b_/a),1)); Dg=M((str(a),0),(0,str(d-b_*b_/a))); Ug=M((1,str(b_/a)),(0,1))
print("LDU==sym2x2?",p(mm(mm(Lg,Dg),Ug))==p(M((str(a),str(b_)),(str(b_),str(d)))))
show("A^-1 for (2,1,2)", inv(M((2,1),(1,2))))
A=M((0,1),(1,1)); print("det",det(A), "A^-1",p(inv(A)))

print("=== Q24")
A=M((1,0),(0,0)); B=M((1,1),(1,1))
show("AB",mm(A,B)); show("BA",mm(B,A)); show("(AB)^T", [list(c) for c in zip(*mm(A,B))])
show("A2-B2", [[A[i][j]**2 for j in range(2)] for i in range(2)])

print("=== Q27")
A=M((1,0,0,0),(2,3,0,0),(1,1,4,0),(1,2,2,5)); print("det",det(A))
print("coeffs", [str(v) for v in mv(inv(A),[1,1,1,1])])
print("check", mv(A,[float(0)]*0 or [v for v in mv(inv(A),[1,1,1,1])]))

print("=== Q28")
R=M((1,0,2,-1,3),(0,1,1,3,0),(0,0,0,0,0))
nb=[[-2,-1,1,0,0],[1,-3,0,1,0],[-3,0,0,0,1]]
print("R*nb:", [mv(R,v) for v in nb])
A=M((1,2,3),(2,4,6),(3,6,9))
_,pv=rref([r[:] for r in A]); print("lam=6 pivots",pv)
A2=M((1,2,3),(2,4,5),(3,6,9)); _,pv2=rref([r[:] for r in A2]); print("lam=5 pivots",pv2,"r=",len(pv2))
RR=M((1,-2,0,0),(0,0,1,0),(0,0,0,1)); print("R*n", [mv(RR,v) for v in [[2,1,0,1]]])

print("=== Q31")
A=M((1,1,1),(1,3,3),(1,3,6))
L=M((1,0,0),(1,1,0),(1,1,1)); D=M((1,0,0),(0,2,0),(0,0,3))
print("LDLt==A?",p(mm(mm(L,D),[list(c) for c in zip(*L)]))==p(A))
print("x", [str(v) for v in mv(inv(A),[1,2,3])])

print("=== Q32")
u=M((1),(2),(3)); A=mm(u,[[1,2,3]]); show("uu^T",A)
print("A^2",p(mm(A,A)),"14A",p([[14*v for v in r] for r in A]))
_,pv=rref([r[:] for r in A]); print("piv",pv)
print("check null:", mv(A,[-2,1,0]), mv(A,[-3,0,1]))
