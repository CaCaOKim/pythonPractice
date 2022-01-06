import sys
sys.stdin=open("RepresentativeValueInput.txt", "rt")

N = int(input())
scores = list(map(int, input().split()))

result = 0
repNum = 0
avg = round(sum(scores)/N)

for i in range(len(scores)):
    gap = abs(scores[i] - avg)
    gapMin = abs(repNum - avg)
    if gap < gapMin: 
        repNum = scores[i]
        result = i + 1
    elif gap == gapMin: 
        if repNum < scores[i]:
            repNum = scores[i]
            result = i + 1

print(avg, result)
