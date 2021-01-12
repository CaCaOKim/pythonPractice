import sys
sys.stdin = open("TitanicGridyInput.txt", "rt")

N, M = map(int, input().split())
person = list(map(int, input().split()))
person.sort()
s = 0
e = N-1
ship = 0

while s <= e:
    if person[s]+person[e] <= M:
        s += 1
        e -= 1
        ship += 1
    else:
        e -= 1
        ship += 1

print(ship)









