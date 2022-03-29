def DFS(n, f):
    print(n, f)

import sys
sys.stdin = open("ProgressionGuessInput.txt", "rt")

N, F = map(int, input().split())

DFS(N, F)

