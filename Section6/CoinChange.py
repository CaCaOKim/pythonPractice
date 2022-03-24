from lib2to3.pgen2 import grammar


def DFS(typeCnt, coinArr, remains):
    global cnt
    

import sys
sys.stdin = open("CoinChangeInput.txt", "rt")

N = int(input())
coins = list(map(int, input().split()))
M = int(input())
cnt = 0

DFS(N, coins, M)
print(cnt)

