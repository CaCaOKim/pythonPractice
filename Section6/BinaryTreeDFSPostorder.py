def DFS(s,max):
    if s>max:
        return
    else:
        DFS(s*2,max)
        DFS(s*2+1,max)
        print(s, end=' ')


DFS(1,7)
print()

