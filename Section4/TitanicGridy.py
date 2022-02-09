import sys
sys.stdin = open("TitanicGridyInput.txt", "rt")

N, M = map(int, input().split())
weight = list(map(int, input().split()))

weight.sort()
lw = 0
rw = N-1
boat = 0

while lw <= rw:
    boat += 1
    if lw == rw:
        break
    if weight[lw] + weight[rw] > M:
        rw -= 1
    elif weight[lw] + weight[rw] <= M:
        lw += 1
        rw -= 1

print(boat)




