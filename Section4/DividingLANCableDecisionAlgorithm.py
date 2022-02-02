def cntLines(arr, l):
    count = 0
    for x in arr:
        count += (x//l)
    return count

import sys
sys.stdin = open("DividingLANCableDecisionAlgorithmInput.txt", "rt")

K, N = map(int, input().split())
lans = []
for _ in range(K):
    lans.append(int(input()))

lv = 0
rv = max(lans)
result = 0

while lv <= rv:
    leng = (lv + rv)//2
    cnt = cntLines(lans, leng)
    if cnt >= N:
        result = leng
        lv = leng + 1
    else:
        rv = leng - 1

print(result)
