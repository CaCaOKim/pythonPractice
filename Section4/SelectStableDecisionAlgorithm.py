import sys
sys.stdin = open("SelectStableDecisionAlgorithmInput.txt", "rt")

N, C = map(int, input().split())
x = list(int(input()) for _ in range(N))
x.sort()

s = 0
e = max(x)

while s<=e:
    mid = (s+e)//2
    horses = 1
    dtn = 0
    check = x[0]
    for i in range(N):
        dtn = x[i] - check
        if dtn >= mid:
            horses += 1
            check = x[i]

    if horses>=C:
        s = mid+1
        result = mid
    else:
        e = mid-1

print(result)
 












