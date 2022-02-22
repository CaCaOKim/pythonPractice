import sys
sys.stdin = open("EmergencyRoomInput.txt", "rt")

N, M = map(int, input().split())
patients = [(idx, dng) for idx, dng in enumerate(list(map(int, input().split())))] 
cnt = 0

while len(patients) > 1:
    if any(patients[0][1] < x[1] for x in patients):
        patients.append(patients.pop(0))
    else:
        maxNum = patients.pop(0)
        cnt += 1
        if maxNum[0] == M:
            break

print(cnt)
