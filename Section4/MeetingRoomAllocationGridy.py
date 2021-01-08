import sys
sys.stdin = open("MeetingRoomAllocationGridyInput.txt", "rt")

n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]
times.sort(key=lambda x:(x[1],x[0]))

cnt = 0
check = 0
for i in range(n):
    if times[i][0] >= check:
        cnt += 1
        check = times[i][1]

print(cnt)




