def DFS(num, sum):
    if num==N and sum==F:
        for x in p:
            print(x, end=' ')
        print()
        sys.exit(0)
    else:
        for i in range(1, N+1):
            if ch[i]==0:
                ch[i] = 1
                p[num] = i
                DFS(num+1, sum+(p[num]*b[num]))
                ch[i] = 0

import sys
sys.stdin = open("ProgressionGuessInput.txt", "rt")

N, F = map(int, input().split())
p = [0]*N
b = [1]*N
ch = [0]*(N+1)
for i in range(1, N):
    b[i] = b[i-1]*(N-i)//i
DFS(0,0)
