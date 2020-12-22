import sys
sys.stdin = open("OnlyNumberOutputInput.txt", "rt")

string = input()
num = 0
for i in range(len(string)):
    if string[i].isdigit():
        num = num*10 + int(string[i])
print(num)

cnt = 0
for j in range(1,num+1):
    if num%j==0:
        cnt += 1
print(cnt)