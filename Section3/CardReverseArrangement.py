import sys
sys.stdin = open("CardReverseArrangementInput.txt", "rt")

cards = list(range(1,21))

for _ in range(10):
    rg = list(map(int, input().split()))
    for i in range((rg[1]-rg[0]+1)//2):
        cards[rg[0]-1+i], cards[rg[1]-1-i] = cards[rg[1]-1-i], cards[rg[0]-1+i]

for i in cards:
    print(i, end=' ')

print()