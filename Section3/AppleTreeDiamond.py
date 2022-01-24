import sys
sys.stdin = open("AppleTreeDiamondInput.txt", "rt")

N = int(input())
maxCnt = N//2
result = 0

for i in range(N):
    apple = list(map(int, input().split()))
    if i <= maxCnt:
        for j in range(maxCnt-i, maxCnt+i+1):
            result += apple[j]
    else:
        for k in range(i-maxCnt, N-i+maxCnt):
            result += apple[k]

print(result)
