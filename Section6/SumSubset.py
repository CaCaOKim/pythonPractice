def DFS(n, s, cnt, arr, tot):
    if s > tot//2:
        return
    if n == cnt:
        if s == (tot-s):
            print("YES")
            sys.exit(0)
    else:
        DFS(n+1, s+arr[n], cnt, arr, tot)
        DFS(n+1, s, cnt, arr, tot)

import sys
sys.stdin = open("SumSubsetInput.txt", "rt")

N = int(input())
nums = list(map(int, input().split()))

total = sum(nums)
DFS(0, 0, N, nums, total)
print("NO")
