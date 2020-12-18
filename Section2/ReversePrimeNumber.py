def reverse(x):
    num = 0
    while(x!=0):
        num = num*10 + x%10
        x //= 10
    return num


def isPrime(x):
    if x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    else:
        return True


import sys
sys.stdin = open("ReversePrimeNumberInput.txt", "rt")

N = int(input())
nums = list(map(int, input().split()))

for i in range(N):
    rev = reverse(nums[i])
    if(isPrime(rev)==True):
        print(rev, end=' ')
print()