import sys
sys.stdin = open("SudokuCheckInput.txt", "rt")

sudoku = [list(map(int, input().split())) for _ in range(9)]
result = "YES"

for i in range(9):
    check1 = [0]*9
    check2 = [0]*9
    for j in range(9):
        check1[sudoku[i][j]-1] = 1
        check2[sudoku[i][j]-1] = 1
    if sum(check1) != 9 or sum(check2) != 9:
        result = "NO"
        break

for i in range(0,9,3):
    for j in range(0,9,3):
        check3 = [0]*9
        for k in range(3):
            for l in range(3):
                check3[sudoku[i+k][j+l]-1] = 1
        if sum(check3) != 9:
            result = "NO"
            break

print(result)