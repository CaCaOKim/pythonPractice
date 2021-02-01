def DFS(s):
    if s>7:
        return
    else:
        DFS(s*2)
        DFS(s*2+1)
        print(s, end=' ')


DFS(1)
print()

