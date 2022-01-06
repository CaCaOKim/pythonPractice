arr = [23,5,3,4,12,1,9,123,36,3,5,2,72,6,8]
result = float('inf') ## 파이썬에서 가장 큰 값
for i in range(len(arr)):
    if arr[i] < result:
        result = arr[i]
print(result)
