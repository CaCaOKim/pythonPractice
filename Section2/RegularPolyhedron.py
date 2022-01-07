import sys
sys.stdin=open("RegularPolyhedronInput.txt", "rt")

N, M = map(int, input().split())
nm = [N, M]
sums = list()

nm.sort
for sum in range(nm[0]+1, nm[1]+2):
    sums.append(sum)

for x in sums:
    print(x, end=' ')
print()
