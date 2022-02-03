import sys
sys.stdin = open("MusicVideoDecisionAlgorithmInput.txt", "rt")

N, M = map(int, input().split())
musics = list(map(int, input().split()))

lv = 0
rv = sum(musics)
result = 0

while lv <= rv:
    mv = (lv + rv)//2
    temp = 0
    cnt = 1
    for x in musics:
        temp += x
        if temp > mv:
            cnt += 1
            temp = x
    if cnt > M:
        lv += 1
    else:
        result = mv
        rv -= 1

print(result)