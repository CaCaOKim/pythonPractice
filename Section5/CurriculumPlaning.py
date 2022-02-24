import sys
sys.stdin = open("CurriculumPlaningInput.txt", "rt")

nece = input()
cnt = int(input())
result = []

for _ in range(cnt):
    curriculum = input()
    temp = nece
    for word in curriculum:
        if temp[0] == word:
            temp = temp[1:]
            if len(temp) == 0:
                break
    if temp == '':
        result.append('YES')
    else:
        result.append('NO')

for i in range(cnt):
    print('#' + str(i+1) + ' ' + result[i])
    

