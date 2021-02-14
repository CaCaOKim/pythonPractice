import sys
import itertools as it
sys.stdin = open("NumbersCombinationInput.txt", "rt")

N, K = map(int, input().split())
num = list(map(int,input().split()))
M = int(input())
cnt = 0

for x in it.combinations(num, K):
    if sum(x)%M==0:
        cnt += 1

print(cnt)
