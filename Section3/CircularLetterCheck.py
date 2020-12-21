import sys
sys.stdin = open("CircularLetterCheckInput.txt", "rt")

N = int(input())

for i in range(N):
    word = input()
    word = word.upper()
    
    # for j in range(len(word)//2):
    #     if word[j] != word[-1-j]:
    #         print("#"+str((i+1))+" NO" )
    #         break
    # else:
    #     print("#"+str((i+1))+" YES" )

    if word == word[::-1]:
        print("#"+str((i+1))+" YES" )
    else:
        print("#"+str((i+1))+" NO" )