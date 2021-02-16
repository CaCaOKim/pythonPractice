def DFS(v):
    global cnt
    if v==N:
        cnt = cnt + 1
    else:
        for i in range(1, N+1):
            if g[v][i]==1 and ch[i]==0:
                ch[i]=1
                DFS(i)
                ch[i]=0

import sys
sys.stdin = open("PathFindingInput.txt", "rt")

N, M = map(int, input().split())
g = [[0]*(N+1) for _ in range(N+1)]
ch = [0]*(N+1)
for i in range(M):
    a, b = map(int, input().split())
    g[a][b]=1
cnt = 0
ch[1] = 1
DFS(1)
print(cnt)




