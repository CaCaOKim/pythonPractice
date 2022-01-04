import sys
sys.stdin=open("KthNumberInput.txt", "rt")

T = int(input())
for t in range(T):
    N, S, E, K = map(int, input().split())
    temp = list(map(int, input().split()))
    temp = temp[S-1:E]
    temp.sort()
    print('#' + str(t+1), temp[K-1])














