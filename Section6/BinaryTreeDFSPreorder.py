def DFS(num):
    if num>7:
        return
    else:
        print(num)
        DFS(num*2)
        DFS(num*2+1)

DFS(1)

