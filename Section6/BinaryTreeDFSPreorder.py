def DFS(s):
    if s>7:
        return
    else:
        print(s, end=' ')
        DFS(s*2)
        DFS(s*2+1)


DFS(1)
print()

