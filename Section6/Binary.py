def DFS(num, res, ten):
    if num==0:
        return res
    else:
        res = res + num%2*ten
        nextNum = num//2
        return DFS(nextNum, res, ten*10)

import sys
sys.stdin = open("BinaryInput.txt", "rt")

N = int(input())

print(DFS(N, 0, 1))

