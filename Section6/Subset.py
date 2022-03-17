def DFS(num, arr, lim):
    if num == lim+1:
        for i in range(1, lim+1):
            if arr[i] == 1:
                print(i, end=' ')
        print()
    else:
        arr[num]=1
        DFS(num+1, arr, lim)
        arr[num]=0
        DFS(num+1, arr, lim)


import sys
sys.stdin = open("SubsetInput.txt", "rt")

N = int(input())
temp = [0]*(N+1)
DFS(1, temp, N)
