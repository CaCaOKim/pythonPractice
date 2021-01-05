import sys
sys.stdin = open("DividingLANCableDecisionAlgorithmInput.txt", "rt")

K, N = map(int, input().split())
cables = list(int(input()) for _ in range(K))
s = 0
e = max(cables)
result = 0

while s<=e:
    quotient = 0
    divide = (s+e)//2
    for i in range(K):
        quotient += cables[i]//divide

    if quotient > N:
        result = divide
        s = divide+1
    elif quotient < N:
        e = divide-1
    else:
        break

print(result)