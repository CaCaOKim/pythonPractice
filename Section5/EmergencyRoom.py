import sys
sys.stdin = open("EmergencyRoomInput.txt", "rt")

N, M = map(int, input().split())
pnt = list(map(int, input().split()))
shadow = [0]*N
shadow[M] = 1
check = 0
result = 0

while check==0:
    if pnt[0]<max(pnt):
        pnt.append(pnt.pop(0))
        shadow.append(shadow.pop(0))
    else:
        pnt.pop(0)
        check = shadow.pop(0)
        result += 1

print(result)


