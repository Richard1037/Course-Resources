from fractions import Fraction as F
def _row(r): return [F(str(r))] if isinstance(r,(int,F)) else [F(str(x)) for x in r]
def M(*rows): return [_row(r) for r in rows]
def mm(A,B): return [[sum(A[i][t]*B[t][j] for t in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def mv(A,x): return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A))]
def det(A):
    n=len(A); B=[r[:] for r in A]; d=F(1)
    for i in range(n):
        p=next((r for r in range(i,n) if B[r][i]!=0),None)
        if p is None: return F(0)
        if p!=i: B[i],B[p]=B[p],B[i]; d=-d
        d*=B[i][i]
        for r in range(i+1,n):
            f=B[r][i]/B[i][i]
            for c in range(i,n): B[r][c]-=f*B[i][c]
    return d
def rref(A):
    A=[r[:] for r in A]; rows=len(A); cols=len(A[0]); r=0; piv=[]
    for c in range(cols):
        if r>=rows: break
        p=next((i for i in range(r,rows) if A[i][c]!=0),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]; pv=A[r][c]; A[r]=[x/pv for x in A[r]]
        for i in range(rows):
            if i!=r and A[i][c]!=0:
                f=A[i][c]; A[i]=[A[i][j]-f*A[r][j] for j in range(cols)]
        piv.append(c); r+=1
    return A,piv
def inv(A):
    n=len(A); B=[A[i]+[F(int(i==j)) for j in range(n)] for i in range(n)]
    R,_=rref(B); return [r[n:] for r in R]
def eye(n): return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def p(A): return [[str(x) for x in r] for r in A]
