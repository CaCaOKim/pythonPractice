import sys
sys.stdin = open("GridCircularNumberInput.txt", "rt")

grid = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

for i in range(7):
    for j in range(3):
        if all(grid[i][j+s]==grid[i][j+4-s] for s in range(2)):
            cnt += 1
        if all(grid[j+s][i]==grid[j+4-s][i] for s in range(2)):
            cnt += 1

print(cnt)