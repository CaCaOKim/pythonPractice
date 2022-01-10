def digit_sum(x):
    num = x % 10
    nextNum = x // 10
    sum = 0

    if nextNum > 0:
        sum = num + digit_sum(nextNum)
    else:
        sum += num

    return sum

import sys
sys.stdin=open("SumOfPositionalNumbersInput.txt", "rt")

N = int(input())
nums = list(map(int, input().split()))
result = list()
maxSum = 0

for x in nums: 
    sum = digit_sum(x)
    if sum > maxSum:
        maxSum = sum
        result = [x]
    elif sum == maxSum:
        result.append(x)

for y in result:
    print(y, end=' ')

print()
