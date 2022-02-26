import sys
sys.stdin = open("AnagramInput.txt", "rt")

w1 = input()
w2 = input()
dic = dict()

for x in w1:
    dic[x] = dic.get(x, 0) + 1
for x in w2:
    dic[x] = dic.get(x, 0) - 1

for x in w1:
    if dic[x] > 0:
        print("NO")
        break
else:
    print("YES")
    
