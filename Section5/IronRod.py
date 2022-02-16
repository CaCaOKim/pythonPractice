import sys
sys.stdin = open("IronRodInput.txt", "rt")

rod = input()

cnt = 0
result = 0

for i in range(len(rod)):
    if rod[i] == '(':
        cnt += 1
    elif rod[i] == ')':
        cnt -= 1
        if rod[i-1] == '(':
            result += cnt
        elif rod[i-1] == ')':
            result += 1

print(result)
