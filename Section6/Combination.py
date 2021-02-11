def DFS(n,s):
    global cnt
    if n==M:
        for i in range(n):
            print(arr[i], end=' ')
        cnt = cnt + 1
        print()
    else:
        for j in range(s, N+1):
            arr[n] = j
            DFS(n+1, j+1)
import sys
sys.stdin = open("CombinationInput.txt", "rt")

N, M = map(int, input().split())
arr = [0]*(N+1)
cnt = 0

DFS(0,1)
print(cnt)


