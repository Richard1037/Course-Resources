Room=[120,40,85,50,100,140,70,100]
st=[0]*8
ans=[0]*4

Stu=list(map(int,input().split()))

cnt=0

def dfs(p=0):
    global cnt
    if p>=4:
        print(*ans)
        cnt+=1
    else:
        for i in range(8):
            if st[i]!=0 or Stu[p]>Room[i]:
                continue
            else:
                st[i]=1
                ans[p]=i+1
                dfs(p+1)
                st[i]=0
    return

dfs()

if cnt==0:
    print("-1")