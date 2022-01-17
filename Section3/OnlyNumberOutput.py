import sys
import math
sys.stdin = open("OnlyNumberOutputInput.txt", "rt")

words = input()
num = 0

for word in words:
    if word.isdecimal():
        num = num*10 + int(word)
print(num)

result = 0
if num < 2:
    print(0)
else:
    x = 1
    while x <= math.sqrt(num):
        if num%x == 0:
            if x**(2) == num:
                result += 1
            else:
                result += 2
        x += 1
    print(result)
