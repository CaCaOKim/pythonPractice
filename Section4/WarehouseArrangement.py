import sys
sys.stdin = open("WarehouseArrangementInput.txt", "rt")

L = int(input())
height = list(map(int, input().split()))
M = int(input())

for _ in range(M):
    height.sort()
    height[0] += 1
    height[L-1] -= 1

height.sort()
result = height[L-1] - height[0]

print(result)




