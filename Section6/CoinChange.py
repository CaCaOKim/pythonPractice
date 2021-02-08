def DFS(n, i, cnt):
    if n==0:
        print(cnt)
    else:
        change = n%coin[i]
        cnt = cnt + n//coin[i]
        DFS(change, i-1, cnt)

import sys
sys.stdin = open("CoinChangeInput.txt", "rt")

N = int(input())
coin = list(map(int, input().split()))
coin.sort()
M = int(input())
cnt = 0

print(coin)
DFS(M,N-1,0)



