import sys
sys.stdin = open("MusicVideoDecisionAlgorithmInput.txt", "rt")

N, M = map(int, input().split())
DVDs = list(map(int, input().split()))

s = 1
e = sum(DVDs)
result = 0

while s<=e:
    mid = (s+e)//2
    
    temp = 0
    cnt = 1
    for i in range(N):
        temp += DVDs[i]
        if temp > mid:
            cnt += 1
            temp = DVDs[i]

    if cnt > M:
        s = mid+1
    else:
        e = mid-1
        result = mid

print(result)
