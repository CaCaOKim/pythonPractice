import sys
sys.stdin = open("DiseGameInput.txt", "tr")

N = int(input())
result = 0

for i in range(N):
    player = list(map(int, input().split()))
    player.sort()
    if player[0] == player[1] == player[2]:
        reward = 10000 + player[1]*1000
    elif player[0] == player[1] or player[2] == player[1]:
        reward = 1000 + player[1]*100
    else:
        reward = max(player)*100
    
    if reward>result:
        result = reward

print(result)