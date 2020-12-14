import sys
sys.stdin=open("RepresentativeValueInput.txt", "rt")

N = int(input())
scores = list(map(int, input().split()))
RV = 0
Df = float('inf')

avr = int((sum(scores)/N) + 0.5)
for idx, score in enumerate(scores):
    if abs(score-avr)<Df:
        Df = abs(score-avr)
        IRV = idx+1
        RV = score
    elif abs(score-avr)==Df and score>RV:
        IRV = idx+1

print(avr, IRV)