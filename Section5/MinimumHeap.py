import sys
import heapq
sys.stdin = open("MinimumHeapInput.txt", "rt")

nums = []
while True:
    N = int(input())
    if N == -1:
        break
    if N == 0:
        if len(nums) == 0:
            print(-1)
        else:
            print(heapq.heappop(nums))
    else:
        heapq.heappush(nums, N)


