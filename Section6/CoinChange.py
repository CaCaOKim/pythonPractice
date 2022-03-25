from lib2to3.pgen2 import grammar


def DFS(c, sum, typeCnt, coinArr, remains):
    global cnt
    if c > cnt:
        return
    if sum > remains:
        return
    if sum == remains:
        if c < cnt:
            cnt = c
    else:
        for i in range(typeCnt):
            DFS(c+1, sum+coinArr[i], typeCnt, coinArr, remains)

import sys
sys.stdin = open("CoinChangeInput.txt", "rt")

N = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
M = int(input())
cnt = 2147000000

DFS(0, 0, N, coins, M)
print(cnt)

