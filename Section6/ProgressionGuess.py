def DFS(num, sum, arr, tempArr, chArr, n, f):
    if num == n and sum == f:
        for x in arr:
            print(x, end=' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if chArr[i] == 0:
                chArr[i] = 1
                arr[num] = i
                DFS(num+1, sum+(arr[num]*tempArr[num]), arr, tempArr, chArr, n, f)
                chArr[i] = 0

import sys
from tabnanny import check
sys.stdin = open("ProgressionGuessInput.txt", "rt")

N, F = map(int, input().split())
prog = [0]*N
temp = [1]*N
checkArr = [0]*(N+1)
for i in range(1, N):
    temp[i] = temp[i-1]*(N-i)//i
DFS(0, 0, prog, temp, checkArr, N, F)


