import sys
sys.stdin = open("AnagramInput.txt", "rt")

word1 = input()
word2 = input()

contain = dict()

for i in range(len(word1)):
    contain[word1[i]] = contain.get(word1[i], 0) + 1
for i in range(len(word2)):
    contain[word2[i]] = contain.get(word2[i], 0) - 1

for i in range(len(word1)):
    if contain.get(word1[i])!=0:
        print("NO")
        break
else:
    print("YES")




