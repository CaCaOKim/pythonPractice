def DFS(num, arr, chArr, n, m):
    global cnt
    if num == m:
        for i in range(num):
            print(arr[i], end=' ')
        print()
        cnt += 1
    else:
        for j in range(1, n+1):
            if chArr[j] == 0:
                chArr[j] = 1
                arr[num] = j
                DFS(num+1, arr, chArr, n, m)
                chArr[j] = 0

import sys
sys.stdin = open("PermutationInput.txt", "rt")

N, M = map(int, input().split())
marbles = [0]*N
check = [0]*(N+1)
cnt = 0
DFS(0, marbles, check, N, M)
print(cnt)
