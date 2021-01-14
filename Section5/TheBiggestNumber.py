import sys
sys.stdin = open("TheBiggestNumberInput.txt", "rt")

num, m = map(int, input().split())
num = list(map(int, str(num)))
arr =[]

for i in range(len(num)):
    while arr and arr[-1]<num[i] and m>0:
        arr.pop()
        m -= 1
    arr.append(num[i])

if m>0:
    arr=arr[:-m]

result = 0
for i in range(len(arr)):
    result *= 10
    result += arr[i]

print(result)
