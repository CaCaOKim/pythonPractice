import sys
sys.stdin = open("SumOfTwoListsInput.txt", "rt")

N = int(input())
list1 = list(map(int, input().split()))
M = int(input())
list2 = list(map(int, input().split()))
list1.append(2417000000)
list2.append(2417000000)
i = j = 0

for _ in range(N+M):
    print(min(list1[0],list2[0]), end=' ')
    if(list1[0]>=list2[0]):
        list2.pop(0)
    else:
        list1.pop(0)

print()




