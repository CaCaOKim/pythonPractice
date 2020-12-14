arr = [23,5,3,4,12,1,9,123,36,3,5,2,72,6,8]
arrMin = float('inf')

for i in arr:
    if i < arrMin:
        arrMin = i

print(arrMin)