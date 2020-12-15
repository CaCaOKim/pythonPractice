import sys
sys.stdin=open("RegularPolyhedronInput.txt", "rt")

N, M = map(int, input().split())
sum = []
sumCnt = [0]*(N+M+1)

for i in range(1,N+1):
    for j in range(1,M+1):
        sumCnt[i+j] += 1

for i in range(2,N+M+1):
    if sumCnt[i] == max(sumCnt):
        print(i, end=' ')

print()