import sys
sys.stdin = open("SumNumbersInput.txt", "rt")

N, M = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
sum = 0
sidx = 0

for i in range(N):
    sum += nums[i]
    if sum > M:
        while sum > M:
            sum -= nums[sidx]
            sidx += 1
            if sum == M:
                cnt += 1
    elif sum == M:
        sum -= nums[sidx]
        sidx += 1
        cnt += 1
        

    
print(cnt)
