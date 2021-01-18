import sys
sys.stdin = open("PostfixCalculationInput.txt", "rt")

formular = input()
stk = []

for i in range(len(formular)):
    if formular[i].isdecimal():
        stk.append(int(formular[i]))
    else:
        if formular[i]=='+':
            stk.append(stk.pop() + stk.pop())
        elif formular[i]=='-':
            stk.append(-stk.pop() + stk.pop())
        elif formular[i]=='*':
            stk.append(stk.pop() * stk.pop())
        elif formular[i]=='/':
            stk.append(1/stk.pop() * stk.pop())

print(stk.pop())





