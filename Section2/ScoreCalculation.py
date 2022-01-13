import sys
sys.stdin = open("ScoreCalculationInput.txt", "rt")

N = int(input())
quiz = list(map(int, input().split()))
mark = 0
score = 0

for x in quiz:
    if x == 0:
        mark = 0
    elif x == 1:
        mark += 1
        score += mark

print(score)
