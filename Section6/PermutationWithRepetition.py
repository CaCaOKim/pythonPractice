def DFS(num):
    global cnt
    
    if num==M:
        for i in range(M):
            print(arr[i], end=' ')
        print()    
        cnt = cnt + 1
    else:
        for j in range(1, N+1):
            arr[num] = j
            DFS(num+1)

import sys
sys.stdin = open("PermutationWithRepetitionInput.txt", "rt")

N, M = map(int, input().split())
arr = [0]*N
cnt = 0

DFS(0)
print(cnt)
