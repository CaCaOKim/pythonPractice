import sys
sys.stdin = open("ReverseSequenceGridyInput.txt", "rt")

N = int(input())
higher = list(map(int, input().split()))
result = [0]*N

for i in range(N):
    seat = 0
    j = 0
    
    while j<=higher[i]:
        if(result[seat]==0):
            j+=1
        seat += 1
    
    result[seat-1] = i+1

for x in result:
    print(x, end=' ')

print()


