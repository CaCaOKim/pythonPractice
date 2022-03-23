def DFS(cnt, arr, max, mcnt):
    global result
    if cnt == mcnt:
        for j in range(mcnt):
            print(arr[j], end=' ')
        print()
        result += 1
    else:
        for i in range(1, max+1):
            arr[cnt] = i
            DFS(cnt+1, arr, max, mcnt)

import sys
sys.stdin = open("PermutationWithRepetitionInput.txt", "rt")

N, M = map(int, input().split())
result = 0
numArr = [0]*M

DFS(0, numArr, N, M)
print(result)
