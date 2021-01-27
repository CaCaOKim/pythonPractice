import heapq as hq
import sys
sys.stdin = open("MaximumHeapInput.txt", "rt")

tree = []

while True:
    num = int(input())

    if num==-1:
        break
    elif num==0:
        if len(tree)==0:
            print(-1)
        else:
            print(-hq.heappop(tree))
    else:
        hq.heappush(tree, -num)