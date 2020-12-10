import sys
sys.stdin=open("KthNumberInput.txt", "rt")

T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums = nums[s-1:e]
    nums.sort()
    if 0<k<=e-s+1:
        print("#"+str(t+1), nums[k-1])
    else:
        print("잘못 입력되었습니다.")




















