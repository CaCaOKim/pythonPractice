import sys
import itertools as it
sys.stdin = open("ProgressionGuessInput.txt", "rt")

N, F = map(int, input().split())
b = [1]*N
cnt = 0

for i in range(1, N):
    b[i] = b[i-1]*(N-i)//i
arr = list(range(1, N+1))
for tmp in it.permutations(arr):
    sum = 0
    for L, x in enumerate(tmp):
        sum += (x*b[L])
    if sum==F:
        for x in tmp:
            print(x, end=' ')
        break
print()
