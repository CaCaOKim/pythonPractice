def digit_sum(x):
    sum = 0
    while(x!=0):
        sum += x%10
        x = x//10
    return sum

import sys
sys.stdin=open("SumOfPositionalNumbersInput.txt", "rt")

N = int(input())
nums = list(map(int, input().split()))
maxsum = 0
result = 0

for i in range(N):
    if digit_sum(nums[i]) > maxsum:
        maxsum = digit_sum(nums[i])
        result = nums[i]

print(result)
