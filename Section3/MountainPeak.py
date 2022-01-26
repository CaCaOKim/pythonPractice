import sys
sys.stdin = open("MountainPeakInput.txt", "rt")

N = int(input())
heights = [[0]*(N+2)]
for idx in range(N):
    heights.append(list(map(int, input().split())))
    heights[idx+1].insert(0, 0)
    heights[idx+1].append(0)
heights.append([0]*(N+2))
result = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        it = heights[i][j]
        if it > heights[i-1][j] and it > heights[i][j-1] and it > heights[i][j+1] and it > heights[i+1][j]:
            result += 1

print(result)
