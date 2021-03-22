import sys
sys.stdin = open("SumSubsetInput.txt", "rt")

def DFS(i, s):
    if s>total//2:
        return
    if i==N:
        if s==total/2:
            print('YES')
            sys.exit(0)
    else:
        DFS(i+1, s+num[i])
        DFS(i+1, s)

N = int(input())
num = list(map(int, input().split()))
print(total)
DFS(0,0)
print("NO")

