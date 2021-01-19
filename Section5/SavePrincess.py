import sys
sys.stdin = open("SavePrincessInput.txt", "rt")

N, K = map(int, input().split())
que = list(range(1,N+1))

while len(que)>1:
    for _ in range(K-1):
        que.append(que.pop(0))
    que.pop(0)

print(que.pop())


