import sys
sys.stdin=open("KthGreatNumberInput.txt", "rt")

N, K = map(int, input().split())
cards = list(map(int, input().split()))
sums = set()
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sums.add(cards[i] + cards[j] + cards[k])
sums = list(sums)
sums.sort(reverse=True)
print(sums[K-1])















