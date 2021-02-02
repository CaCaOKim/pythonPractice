def DFS(num):
    if num==N+1:
        for i in range(1, N+1):
            if check[i]==1:
                print(i, end=' ')
        print()
    else:
        check[num]=1
        DFS(num+1)
        check[num]=0
        DFS(num+1)


import sys
sys.stdin = open("SubsetInput.txt", "rt")

N = int(input())
check = [0]*(N+1)
DFS(1)



