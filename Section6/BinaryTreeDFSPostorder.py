def DFS(num):
    if num>7:
        return
    else:
        DFS(num*2)
        DFS(num*2+1)
        print(num)

DFS(1)


