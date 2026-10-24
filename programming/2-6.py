def get_score(dice):

    cnt = [0]*7 
    for x in dice:
        cnt[x] += 1   
    if cnt[4]==4 and cnt[1]==2:
        return 2048
    if cnt[4]==6:
        return 1024
    if cnt[1]==6:
        return 512
    if cnt[2]==6:
        return 256
    if cnt[4]==5:
        return 128
    if cnt[1]==5 or cnt[2]==5 or cnt[3]==5 or cnt[4]==5 or cnt[5]==5 or cnt[6]==5:
        return 64
    if cnt[4]==4:
        return 32
    if cnt[1]==1 and cnt[2]==1 and cnt[3]==1 and cnt[4]==1 and cnt[5]==1 and cnt[6]==1:
        return 16
    if cnt[4]==3:
        return 8
    if cnt[2]==4:
        return 4
    if cnt[4]==2:
        return 2
    if cnt[4]==1:
        return 1
    return 0

n = int(input())
total = 0
game_over = False

for _ in range(n):
    if game_over:
        break
    parts = list(map(int, input().split()))
    s = get_score(parts)
    total += s
    if s == 0:
        game_over = True

print(f"{total:x}")
