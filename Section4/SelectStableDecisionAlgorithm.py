import sys
sys.stdin = open("SelectStableDecisionAlgorithmInput.txt", "rt")

N, C = map(int, input().split())
stable = []
for _ in range(N):
    stable.append(int(input()))
stable.sort()
lv = 1
rv = stable[N-1]

while lv <= rv:
    mv = (lv + rv)//2
    cnt = 1
    temp = stable[0]
    for i in range(1, N):
        if stable[i] - temp >= mv:
            cnt += 1
            temp = stable[i]
    if cnt >= C:
        result = mv
        lv = mv + 1
    else:
        rv = mv - 1

print(result)
 












