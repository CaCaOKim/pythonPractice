def checkCir(arr):
    result = True
    for idx in range(len(arr)//2):
        if arr[idx] != arr[len(arr)-1-idx]:
            result = False
            break
    return result

import sys
sys.stdin = open("GridCircularNumberInput.txt", "rt")

grid = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

for i in range(7):
    for j in range(3):
        hnums = []
        vnums = []
        for k in range(5):
            hnums.append(grid[i][j+k])
            vnums.append(grid[j+k][i])
        if checkCir(hnums):
            cnt += 1
        if checkCir(vnums):
            cnt += 1

print(cnt)


