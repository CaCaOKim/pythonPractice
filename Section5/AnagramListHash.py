import sys
sys.stdin = open("AnagramListHashInput.txt", "rt")

w1 = input()
w2 = input()
dic1 = [0]*52
dic2 = [0]*52

for x in w1:
    if x.isupper():
        dic1[ord(x) - 65] += 1
    else:
        dic1[ord(x) - 71] += 1
for y in w2:
    if y.isupper():
        dic2[ord(y) - 65] += 1
    else:
        dic2[ord(y) - 71] += 1

for i in range(52):
    if dic1[i] != dic2[i]:
        print("NO")
        break
else:
    print("YES")

