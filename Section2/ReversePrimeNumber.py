def reverse(x):
    val = 0
    while x > 0:
        val = val*10 + x%10
        x = x//10
    return val

def isPrime(y):
    if y == 0 or y == 1:
        return False
    for i in range(2, y//2 + 1):
        if y%i == 0:
            return False
    else:
        return True

import sys
sys.stdin = open("ReversePrimeNumberInput.txt", "rt")

N = int(input())
nums = list(map(int, input().split()))

for x in nums:
    revX = reverse(x)
    if isPrime(revX):
        print(revX, end = ' ')

print()