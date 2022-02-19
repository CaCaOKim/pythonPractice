from cmath import sin
import sys
from unicodedata import decimal
sys.stdin = open("PostfixExpressionInput.txt", "rt")

exp = input()
sign = []
result = ""

for x in exp:
    if x.isdigit():
        result += x
    else:
        if x == '(':
            sign.append(x)
        elif x == '*' or x == '/':
            while sign and (sign[-1] == '*' or x == '/'):
                result += sign.pop()
            sign.append(x)
        elif x == '+' or x == '-':
            while sign and sign[-1] != '(':
                result += sign.pop()
            sign.append(x)
        elif x == ')':
            while sign and sign[-1] != '(':
                result += sign.pop()
            sign.pop()

while sign:
    result += sign.pop()

print(result)


