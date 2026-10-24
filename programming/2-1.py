lst=input().split()

x,y,c=int(lst[0]),int(lst[1]),lst[2]

if c=='+':
    print(x+y)
elif c=='-':
    print(x-y)
elif c=='*':
    print(x*y)
elif c=='/':
    print("NO" if y==0 else (x//y))
elif c=='%':
    print("NO" if y==0 else (x%y))
else :
    print("NO")
