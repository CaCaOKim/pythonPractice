import sys
sys.stdin = open("IncreasingSequenceGridyInput.txt", "rt")

N = int(input())
nums = list(map(int, input().split()))
s = 0
e = N-1
LR = ""
maxNum = 0
temp = []

while s<=e:
    if nums[s] > maxNum:
        temp.append((nums[s],"L"))
    if nums[e] > maxNum:
        temp.append((nums[e],"R"))
    temp.sort()
    if len(temp) == 0:
        break
    else:
        LR += temp[0][1]
        maxNum = temp[0][0]
        
        if temp[0][1] == "L":
            s += 1
        else:
            e-= 1

        temp.clear()

print(len(LR))
print(LR)




