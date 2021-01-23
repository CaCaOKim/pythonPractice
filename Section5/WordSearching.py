import sys
sys.stdin = open("WordSearchingInput.txt", "rt")

N = int(input())
pre = list(input() for _ in range(N))

for _ in range(N-1):
    pre.remove(input())

print(pre.pop())

