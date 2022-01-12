def calPrize(arr):
    if arr[0] == arr[1]:
        if arr[1] == arr[2]:
            return 10000 + arr[2]*1000
        else:
            return 1000 + arr[1]*100
    else:
        if arr[1] == arr[2]:
            return 1000 + arr[1]*100
        else:
            return arr[0]*100

import sys
sys.stdin = open("DiseGameInput.txt", "tr")

N = int(input())
max = 0
for i in range(N):
    diceDots = list(map(int, input().split()))
    diceDots.sort(reverse=True)
    prize = calPrize(diceDots)
    if prize > max:
        max = prize
print(max)

