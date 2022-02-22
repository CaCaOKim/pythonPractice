import sys
sys.stdin = open("SavePrincessInput.txt", "rt")

N, K = map(int, input().split())
princes = []
for i in range(1, N+1):
    princes.append(i)

while len(princes) > 1:
    for j in range(K-1):
        princes.append(princes.pop(0))
    princes.pop(0)

print(princes[0])
