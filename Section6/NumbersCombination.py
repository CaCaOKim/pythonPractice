def DFS(L, s, sum):
    global cnt
    if L==K:
        if sum%M==0:
            cnt = cnt + 1
    else:
        for j in range(s, N):
            DFS(L+1, j+1, sum+num[j])


import sys
sys.stdin = open("NumbersCombinationInput.txt", "rt")

N, K = map(int, input().split())
num = list(map(int,input().split()))
M = int(input())
cnt = 0

DFS(0,0,0)
print(cnt)
