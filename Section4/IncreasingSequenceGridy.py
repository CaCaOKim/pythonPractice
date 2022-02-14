import sys
sys.stdin = open("IncreasingSequenceGridyInput.txt", "rt")

N = int(input())
nums = list(map(int, input().split()))

cnt = 0
dir = ''
min = 0
ln = 0
rn = N - 1

while ln <= rn:
    temp = []
    if nums[ln] > min:
        temp.append((nums[ln], 'L'))
    if nums[rn] > min:
        temp.append((nums[rn], 'R'))
    temp.sort()
    if len(temp) == 0:
        break
    else:
        dir += temp[0][1]
        cnt += 1
        min = temp[0][0]
        if temp[0][1] == 'L':
            ln += 1
        elif temp[0][1] == 'R':
            rn -= 1
    
print(cnt)
print(dir)


