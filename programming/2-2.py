s=input()

ck,now,res=0,1,0

for c in s:
    if c.isdigit():
        # print(f"{c}\n")
        if now<=9:
            res+=int(c)*now
            now+=1
        else:
            ck=int(c)
    elif c=='X' and now==10:
        ck=10

res%=11

# print(f"res={res},ck={ck}")

if ck==res:
    print("Right")
else:
    if res<10:
        print(s[:-1]+str(res))
    else:
        print(s[:-1]+"X")
