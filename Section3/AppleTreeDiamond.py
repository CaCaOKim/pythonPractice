import sys
sys.stdin = open("AppleTreeDiamondInput.txt", "rt")

N = int(input())
fields = []
for _ in range(N):
    fields.append(list(map(int, input().split())))
result = 0

for i in range(N):
    if i <= N//2:
        for j in range(N//2-i,N//2+i+1):
            result += fields[i][j]
    if i > N//2:
        for j in range(i-N//2,N-(i-N//2)):
            result += fields[i][j]

print(result)