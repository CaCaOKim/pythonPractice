import sys
sys.stdin = open("CurriculumPlaningInput.txt", "rt")

req = input()
N = int(input())

for i in range(N):
    curriculum = input()
    copy = list(i for i in req)
    result = "NO"

    for j in range(len(curriculum)):
        if copy and curriculum[j]==copy[0]:
            copy.pop(0)
        else:
            if copy and curriculum[j] in copy:
                break
            
            
        if copy:
            pass
        else:
            result="YES"
        
    print("#" + str(i+1) + " " + result)


