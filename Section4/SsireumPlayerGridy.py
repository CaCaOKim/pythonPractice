import sys
sys.stdin = open("SsireumPlayerGridyInput.txt", "rt")

N = int(input())
players = []
for _ in range(N):
    h, w = map(int, input().split())
    players.append((h, w))
players.sort(reverse=True)

cnt = 0
maxW = 0

for h, w in players:
    if w > maxW:
        cnt += 1
        maxW = w

print(cnt)