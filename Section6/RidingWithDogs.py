def DFS(i, sum, temp, mw, cnt, arr, tot):
    global result
    if sum + (tot-temp) < result:
        return
    if sum > mw:
        return
    if i == cnt:
        if sum > result:
            result = sum
    else:
        DFS(i+1, sum+arr[i], temp+arr[i], mw, cnt, arr, tot)
        DFS(i+1, sum, temp+arr[i], mw, cnt, arr, tot)

import sys
sys.stdin = open("RidingWithDogsInput.txt", "rt")

C, N = map(int, input().split())
dogs = list(int(input()) for _ in range(N))
total = sum(dogs)
result = -2147000000

DFS(0, 0, 0, C, N, dogs, total)
print(result)