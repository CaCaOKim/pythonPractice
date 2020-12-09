def std_weight(height, gender):
    
    if(gender=="M"):
        weight = round((float(height)*0.01) * (float(height)*0.01) *22, 2)
        gender = "남자"
    elif(gender=="W"):
        weight = round((float(height)*0.01) * (float(height)*0.01) *21, 2)
        gender = "여자"
    else:
        print("잘못 입력하셨습니다. 성별은 M 또는 W입니다.")
        weight = 0
        gender = " "
    
    return height, gender, weight

height, gender, weight = std_weight(input("당신의 키는?(cm) "), input("당신의 성별은?(M/W) "))
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))