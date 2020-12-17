import sys
sys.stdin=open("CountPrimeNumberEratosthenesSieveInput.txt", "rt")

N = int(input())
nums = [0]*(N+1)
result = 0
for i in range(2, N+1):
    if nums[i]==0:
        result += 1
        for j in range(i, N+1, i):
            nums[j] = 1

print(result)