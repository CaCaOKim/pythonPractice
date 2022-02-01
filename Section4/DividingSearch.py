import sys
sys.stdin = open("DividingSearchInput.txt", "rt")

N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

# print(nums.index(M) + 1)

li = 0
ri = N - 1

while li <= ri:
    mi = (li+ri)//2
    if nums[mi] > M:
        ri = mi - 1
    elif nums[mi] < M:
        li = mi + 1
    else:
        print(mi + 1)
        break