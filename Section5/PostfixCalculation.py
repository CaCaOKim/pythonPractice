from curses.ascii import isdigit
import sys
sys.stdin = open("PostfixCalculationInput.txt", "rt")

exp = input()
nums = []

for x in exp:
    if x.isdigit():
        nums.append(int(x))
    else: 
        if x == '+':
            b = nums.pop()
            a = nums.pop()
            nums.append(a + b)
        elif x == '-':
            b = nums.pop()
            a = nums.pop()
            nums.append(a - b)
        elif x == '*':
            b = nums.pop() 
            a = nums.pop()
            nums.append(a * b)
        elif x == '/':
            b = nums.pop()
            a = nums.pop()
            nums.append(a / b)
            
print(nums[0])
