from re import M
import sys
sys.stdin = open("DriedPersimmonSandglassInput.txt", "rt")

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
M = int(input())

for _ in range(M):
    turn = list(map(int, input().split()))
    idx = turn[0]-1
    if turn[1] == 0:
        for _ in range(turn[2]):
            grid[idx].append(grid[idx].pop(0))
    if turn[1] == 1:
        for _ in range(turn[2]):
            grid[idx].insert(0, grid[idx].pop(N-1))
            
result = 0
for i in range(N):
    if i <= N//2:
        for j in range(i, N-i):
            result += grid[i][j]
    else:
        for k in range(N-1-i, i+1):
            result += grid[i][k]

print(result)
