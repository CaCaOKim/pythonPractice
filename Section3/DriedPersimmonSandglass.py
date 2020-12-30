import sys
sys.stdin = open("DriedPersimmonSandglassInput.txt", "rt")

N = int(input())
fields = []
for i in range(N):
    fields.append(list(map(int, input().split())))
M = int(input())

for _ in range(M):
    move = list(map(int, input().split()))
    row = move[0]-1
    if move[1]==0:
        for _ in range(move[2]):
            fields[row].append(fields[row].pop(0))
    elif move[1]==1:
        for _ in range(move[2]):
            fields[row].insert(0, fields[row].pop())
    else:
        pass

result = 0
s = 0
for i in range(N):
    for j in range(s,N-s):
            result += fields[i][j]
    if i<N//2:
            s += 1
    else:
            s -= 1

print(result)