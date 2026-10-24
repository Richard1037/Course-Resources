from _mx import M, mm, mv, det, rref, inv, eye, p
def show(t,A): print(t,*[r for r in p(A)],sep='\n   ')
def hb(TL,TR,BL,BR): return [[*TL[i],*TR[i]] for i in range(len(TL))]+[[*BL[i],*BR[i]] for i in range(len(BL))]
def neg(X): return [[-v for v in r] for r in X]

print("=== Q14(3) variant A=[[I,O],[-A1,I]]")
A1=M((2,-1),(1,3)); I2=eye(2); O=M((0,0),(0,0))
Av=hb(I2,O,neg(A1),I2)
B=M((1,0,0,3),(-1,2,1,-1),(2,0,1,2),(0,1,-1,0))
show("AB(var)",mm(Av,B))

print("=== Q16 general b: is c1=b1, c3=b2-2b1, c5=5b1-3b2+b3 ?")
A=M((1,2,0,-1,0),(2,4,1,1,0),(1,2,3,8,1),(0,0,1,3,2))
import random; random.seed(7)
for trial in range(5):
    xt=[random.randint(-4,4) for _ in range(5)]
    b=mv(A,xt)                      # guaranteed in C(A)
    Aug=[A[i]+[b[i]] for i in range(4)]
    R,_=rref(Aug)
    c=[R[i][5] for i in range(4)]
    b1,b2,b3,b4=[str(v) for v in b]
    pred=[b[0], None, b[1]-2*b[0], None, 5*b[0]-3*b[1]+b[2]]
    print("b=",[str(v) for v in b],"cond=",-8*b[0]+5*b[1]-2*b[2]+b[3],
          "c=",[str(v) for v in c],"pred=",[str(v) for v in pred if v is not None])

print("=== Q28(3): R=[[1,0,0,-2],[0,1,0,-1],[0,0,1,0]] null space")
R=M((1,0,0,-2),(0,1,0,-1),(0,0,1,0))
RR,pv=rref([r[:] for r in R]); print("already RREF?",p(RR)==p(R),"piv",pv)
print("R n =",mv(R,[2,1,0,1]))
nlp,_=rref([r[:] for r in [list(c) for c in zip(*R)]])
print("N basis check: solve R x=0 ->", [str(v) for v in [2,1,0,1]])

print("=== Q2 D^-1")
D=M((1,0,0),(-1,1,0),(0,-1,1)); Di=M((1,0,0),(1,1,0),(1,1,1))
print("Di*D==I?",p(mm(Di,D))==p(eye(3)),"D*Di==I?",p(mm(D,Di))==p(eye(3)))
print("D*(1,4,9)=",mv(D,[1,4,9]),"Di*(1,1,1)=",mv(Di,[1,1,1]))

print("=== Q5 N powers")
N=M((0,2,0,0),(0,0,2,0),(0,0,0,2),(0,0,0,0))
N2=mm(N,N); N3=mm(N2,N); N4=mm(N2,N2)
show("N2",N2); show("N3",N3); show("N4",N4)

print("=== Q8")
A=M((1,2,3),(4,5,6),(7,8,10)); D=M((2,0,0),(0,"1/3",0),(0,0,1))
show("DA",mm(D,A)); show("AD",mm(A,D))
E=M((1,0,0),(0,1,0),(0,0,1)); E[1][0]=3
show("E",E); show("EA",mm(E,A)); show("AE",mm(A,E))
P=M((1,0,0),(0,0,1),(0,1,0)); show("PA",mm(P,A)); show("AP",mm(A,P))
print("E21(1)*[[1,0],[0,0]] =", p(mm(M((1,0),(1,1)),M((1,0),(0,0)))))

print("=== Q9 AB,BA")
A=M((1,0,2),(3,1,-1)); B=M((1,2),(0,1),(2,-1))
show("AB",mm(A,B)); show("BA",mm(B,A))

print("=== Q13 strict example")
A=M((1,0),(0,0)); B=M((0,0),(1,0)); show("AB",mm(A,B))
_,pa=rref([r[:] for r in A]); _,pb2=rref([r[:] for r in B]); _,pab=rref([r[:] for r in mm(A,B)])
print("r(A)",len(pa),"r(B)",len(pb2),"r(AB)",len(pab))

print("=== Q19 concrete A=[1 0 0], B=(1,1,0)^T")
Ar=M((1,0,0)); Br=M((1),(1),(0))
print("AB", p(mm(Ar,Br)), "BA", p(mm(Br,Ar)))
I3=eye(3); I1=eye(1)
M1=[[I1[0][j]-mm(Ar,Br)[0][j] for j in range(1)]]
M2=[[I3[i][j]-mm(Br,Ar)[i][j] for j in range(3)] for i in range(3)]
show("I1-AB",M1); show("I3-BA",M2)
# identity check with invertible case: use A=[[1,0],[0,1],[1,0]]? skip
