import sys
sys.stdin = open("SsireumPlayerGridyInput.txt", "rt")

N = int(input())
player = [list(map(int, input().split())) for _ in range(N)]

player.sort(key=lambda x:-x[0])

cnt = 0
mw = 0
for i in range(N):
    if player[i][1] > mw:
        cnt += 1
        mw = player[i][1]

print(cnt)




