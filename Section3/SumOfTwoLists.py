import sys
sys.stdin = open("SumOfTwoListsInput.txt", "rt")

N = int(input())
nList = list(map(int, input().split()))
M = int(input())
mList = list(map(int, input().split()))

result = nList + mList
result.sort()

for x in result:
    print(x, end=' ')
print()

