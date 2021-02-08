def DFS(num):
    global cnt
    if num>=M:
        for i in range(num):
            print(arr[i], end=' ')
        print()
        cnt = cnt + 1
    else:
        for j in range(1, N+1):
            if check[j]==0:
                check[j] = 1
                arr[num] = j
                DFS(num+1)
                check[j] = 0

import sys
sys.stdin = open("PermutationInput.txt", "rt")

N, M = map(int, input().split())
arr = [0]*N
check = [0]*(N+1)
cnt = 0

DFS(0)
print(cnt)

