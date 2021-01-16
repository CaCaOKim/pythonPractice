import sys
sys.stdin = open("IronRodInput.txt", "rt")

iron = input()
cnt = 0
result = 0

for i in range(len(iron)):
    if iron[i]=='(':
        cnt += 1
    elif iron[i]==')':
        cnt -= 1
        if iron[i-1]=='(':
            result += cnt
        elif iron[i-1]==')':
            result += 1

print(result)


