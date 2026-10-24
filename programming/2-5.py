n=int(input())
data=[]
ans=[]

for i in range(n):
    lst=input().split()
    data.append([lst[0],int(lst[1]),int(lst[2])])

for i in range(0,10000):
    num=f"{i:04d}"
    ts=n
    for j in range(n):
        _num=data[j][0]
        c1,c2=data[j][1],data[j][2]
        cnt1,cnt2=0,0
        for k in range(4):
            if num[k]==_num[k]:
                cnt2+=1
        buc1=[0]*10
        buc2=[0]*10
        for k in range(4): 
            buc1[int(num[k])]+=1
            buc2[int(_num[k])]+=1

        for k in range(10): cnt1+=min(buc1[k],buc2[k])
        if c1!=cnt1 or c2!=cnt2:
            ts-=1
            break
    if(ts==n):
        ans.append(num)
    if(len(ans)>1): break

print(str(ans[0]) if len(ans)==1 else "Not sure")

