import sys
sys.stdin = open("WordSearchingInput.txt", "rt")

N = int(input())
words = []

for _ in range(N):
    words.append(input())
for _ in range(N-1):
    words.remove(input())

print(words[0])
