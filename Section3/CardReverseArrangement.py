import sys
sys.stdin = open("CardReverseArrangementInput.txt", "rt")

cards = list(range(1, 21))
for _ in range(10):
    ai, bi = map(int, input().split())
    for i in range((bi-ai)//2 + 1):
        cards[ai-1+i], cards[bi-1-i] = cards[bi-1-i], cards[ai-1+i]

for x in cards:
    print(x, end = ' ')
print()