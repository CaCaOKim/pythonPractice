import sys
sys.stdin = open("MountainPeakInput.txt", "rt")

N = int(input())
fields = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    fields[i].append(0)
    fields[i].insert(0, 0)
fields.append([0]*(N+2))
fields.insert(0, [0]*(N+2))

cnt = 0
x = [1, 0, -1, 0]
y = [0, 1, 0, -1]
for i in range(1,N+1):
    for j in range(1, N+1):
        if all(fields[i][j]>fields[i+x[k]][j+y[k]] for k in range(4)):
            cnt += 1

print(cnt)