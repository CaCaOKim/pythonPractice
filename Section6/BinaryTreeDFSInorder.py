def DFS(num):
    if num>7:
        return
    else:
        DFS(num*2)
        print(num)
        DFS(num*2+1)


DFS(1)

