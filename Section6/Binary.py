def binary(num):
    if num > 1:
        return binary(num//2) + str(num%2)
    else:
        return str(num%2)

import sys
sys.stdin = open("BinaryInput.txt", "rt")

N = int(input())
print(binary(N))
