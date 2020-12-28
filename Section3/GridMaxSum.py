import sys
sys.stdin = open("GridMaxSumInput.txt", "rt")

N = int(input())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))
maxSum = 0

for i in range(N):
    rowSum = 0
    colSum = 0
    for j in range(N):
        rowSum += grid[i][j]
        colSum += grid[j][i]
    maxSum = max(maxSum, rowSum, colSum)

dign1 = 0
dign2 = 0
for i in range(N):
    dign1 += grid[i][i]
    dign2 += grid[i][N-1-i]
maxSum = max(maxSum, dign1, dign2)

print(maxSum)




