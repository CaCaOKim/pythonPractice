import sys
sys.stdin = open("CircularLetterCheckInput.txt", "rt")

N = int(input())

for i in range(N):
    word = input().lower()
    # if word == word[::-1]: # 단어를 리버스시키는 함수
    for j in range(len(word)//2):
        if word[j] != word[-j-1]:
            print('#' + str(i+1) + ' ' + 'NO')
            break
    else:
        print('#' + str(i+1) + ' ' + 'YES')