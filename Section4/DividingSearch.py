def div(nums,s,e,sch):
    divNum = (s+e)//2
    if nums[divNum] == sch:
        return divNum
    elif nums[divNum] > sch:
        e = divNum - 1
        return div(nums,s,e,sch)
    else:
        s = divNum + 1
        return div(nums,s,e,sch)
       
import sys
sys.stdin = open("DividingSearchInput.txt", "rt")

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

print(div(nums,0,N-1,M)+1)
