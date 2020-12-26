import sys
sys.stdin = open("SumNumbersInput.txt", "rt")

N, M = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
begin = 0
end = 1
total = A[0] + A[1]

while True:
    if total<M:
        end += 1
        if end==M:
            break
        total += A[end]
    else:
        if total==M:
            cnt += 1
        total -= A[begin]
        begin += 1

print(cnt)