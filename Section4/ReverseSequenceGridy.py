import sys
sys.stdin = open("ReverseSequenceGridyInput.txt", "rt")

N = int(input())
seq = list(map(int, input().split()))
result = []

while N > 0:
   result.insert(seq[N - 1], N)
   N -= 1

for x in result:
    print(x, end=' ')

print() 
