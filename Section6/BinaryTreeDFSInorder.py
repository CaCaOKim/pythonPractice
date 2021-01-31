def DFS(s):
    if s>7:
        return
    else:
        DFS(s*2)
        print(s, end=' ')
        DFS(s*2+1)


DFS(1)
print()

