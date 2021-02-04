def DFS(n, sm):
    global mx
    if sm>C:
        return
    if n==N:
        if sm>mx:
            mx=sm
    else:
        DFS(n+1, sm+dog[n])
        DFS(n+1, sm)

import sys
sys.stdin = open("RidingWithDogsInput.txt", "rt")

C, N = map(int, input().split())
dog = list(int(input()) for _ in range(N))
mx = 0

DFS(0, 0)
print(mx)


