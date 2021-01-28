def binary(n):
    next = n//2
    if n==0:
        return
    else:
        binary(next)
        print(n%2, end='')

import sys
sys.stdin = open("BinaryInput.txt", "rt")

N = int(input())

binary(N)
print()
