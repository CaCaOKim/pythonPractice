import sys
sys.stdin = open("MusicVideoDecisionAlgorithmInput.txt", "rt")

N, M = map(int, input().split())
musics = list(map(int, input().split()))

s = 1
e = sum(musics)
result = 0

while s<=e:
    mid = (s+e)//2
    
    temp = 0
    cnt = 1
    for i in range(N):
        temp += musics[i]
        if temp > mid:
            cnt += 1
            temp = musics[i]

    if mid>=max(musics) and cnt <= M:
        e = mid-1
        result = mid
    else:
        s = mid+1
        
print(result)
