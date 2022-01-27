import sys
sys.stdin = open("SudokuCheckInput.txt", "rt")

sudoku = [list(map(int, input().split())) for _ in range(9)]
result = 'YES'

for i in range(9):
    hch = [0]*9
    vch = [0]*9
    for j in range(9):
        hch[sudoku[i][j]-1] = 1
        vch[sudoku[j][i]-1] = 1
    if sum(hch) != 9 or sum(vch) != 9:
        result = 'NO'
        break    

if result == 'YES':
    for k in range(3):
        for l in range(3):
            if result == 'YES':
                sch = [0]*9
                for m in range(3):
                    for n in range(3):
                        sch[sudoku[m+k*3][n+l*3]-1] = 1
                if sum(sch) != 9:
                    result = 'NO'
                    break
print(result)
