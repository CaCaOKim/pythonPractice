def DFS(n):
    pass

import sys
sys.stdin = open("AdjacencyMatrixInput.txt", "rt")

N, M = map(int, input().split())
g = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    g[a][b] = c


for i in range(1, N+1):
    for j in range(1, N+1):
        print(g[i][j], end=' ')
    print()

