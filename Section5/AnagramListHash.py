import sys
sys.stdin = open("AnagramListHashInput.txt", "rt")

word1 = input()
word2 = input()

ascList1 = [0]*52
ascList2 = [0]*52

for i in range(len(word1)):
    if word1[i].isupper():
        ascList1[ord(word1[i])-65] += 1
    else:
        ascList1[ord(word1[i])-71] += 1

for i in range(len(word2)):
    if word2[i].isupper():
        ascList2[ord(word2[i])-65] += 1
    else:
        ascList2[ord(word2[i])-71] += 1

for i in range(52):
    if ascList1[i]!=ascList2[i]:
        print("NO")
        break
else:
    print("YES")


