import sys
sys.stdin = open("ScoreCalculationInput.txt", "rt")

N = int(input())
check = list(map(int, input().split()))
score = 0

for i in range(N):
    if check[i] == 1:
        score += 1
        check[i] = score
    elif check[i] == 0:
        score = 0

print(sum(check))
