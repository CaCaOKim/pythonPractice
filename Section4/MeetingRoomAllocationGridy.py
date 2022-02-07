import sys
sys.stdin = open("MeetingRoomAllocationGridyInput.txt", "rt")

N = int(input())
mt = []
for i in range(N):
    s, e = map(int, input().split())
    mt.append((s, e))
mt.sort(key=lambda x : (x[1], x[0]))
et = 0
cnt = 0
for s, e in mt:
    if s >= et:
        et = e
        cnt += 1

print(cnt)



