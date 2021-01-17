import sys
sys.stdin = open("PostfixExpressionInput.txt", "rt")

formula = input()
stk = []
result = ""

for i in range(len(formula)):
    if formula[i].isdecimal():   #숫자인가?
        result += formula[i]
    else:
        if formula[i]=='(':
            stk.append(formula[i])
        elif formula[i]=='*' or formula[i]=='/':
            while stk and (stk[-1]=='*' or stk[-1]=='/') :
                result += stk.pop()
            stk.append(formula[i])
        elif formula[i]=='+' or formula[i]=='-':
            while stk and stk[-1]!='(':
                result += stk.pop()
            stk.append(formula[i])
        elif formula[i]==')':
            while stk and stk[-1]!='(':
                result += stk.pop()
            stk.pop()

while stk:
    result += stk.pop()

print(str(result))




