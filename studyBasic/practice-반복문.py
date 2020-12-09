#for
for waiting_no in range(5):    # 0 1 2 3 4
    print("대기번호 : {}".format(waiting_no))

starbucks = ["아이언맨", "토르", "캡틴아메리카", "헐크"]
for costomer in starbucks:
    print("{}님, 커피가 준비되었습니다.".format(costomer))


#while
customer = "토르"
index = 5
while index >= 0:
    if index == 0:
        print("커피는 폐기처분되었습니다.")
    else:
        print("{0}님, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    
customer = "아이언맨"
TF = True
while TF:
    print("{0}님, 커피가 준비되었습니다. {1}번 호출되었습니다.".format(customer, index))
    index += 1
    TF = False

person = "Unkown"
while person != customer:
    print("{0}님, 커피가 준비되었습니다.".format(customer))
    person = "아이언맨" #input("이름이 어떻게 되세요? ")


#continue, break
absent = [2,5]
no_book = [7]
for student in range(1,11):   #1 2 3 4 5 6 7 8 9 10
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {}번 학생, 교무실로 따라와".format(student))
        break
    print("{}번 학생, 책 읽어보세요".format(student))


#한 줄 for
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

students = ["Ironman", "Thor", "Captain America", "Hulk"]
students = [len(i) for i in students]
print(students)

students = ["Ironman", "Thor", "Captain America", "Hulk"]
students = [i.upper() for i in students]
print(students)








