import sys
sys.stdin = open("GridMaxSumInput.txt", "rt")

N = int(input())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))
max = 0
sumld = 0
sumrd = 0

for i in range(N):
    sumh = 0
    sumv = 0
    for j in range(N):
        sumh += grid[i][j]
        sumv += grid[j][i]
    if sumh > max:
        max = sumh
    if sumv > max:
        max = sumv
    sumld += grid[i][i]
    sumrd += grid[i][N-1-i]
if sumld > max:
    max = sumld
if sumrd > max:
    max = sumrd

print(max)
