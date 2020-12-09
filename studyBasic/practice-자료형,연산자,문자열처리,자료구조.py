#숫자형
print(5)
print(-10)
print(3.14)
print(32450000)
print(5+3)
print(5*6)
print(5*(3+1))
print()
print(-5.21*2)
print(5/2)
print(7%4)


#문자
print('글자')
print('word'*8)
print("hi "*5)


#참/거짓
print(3<5)
print(9<2)
print(True)
print(False)
print(not False)
print(not 3<5)


#캐릭터을 소개해주세요
movie = "주토피아"
kind = "나무늘보"
name = " 플레쉬"
age = 5
job = "공무원"
is_adult = age >= 3

print(name+"는 "+movie+"에 나오는"+kind+"에요")
print("나이는 "+str(age)+"살이고 "+job+"이랍니다.")
print(name+"은 어른일까요?"+str(is_adult))


#연산자
print(2+3)
print(2-7)
print(2*6)
print(9/3)

print(3**3)   #3^2
print(7%2)   #나머지
print(7//2)   #몫

print(2 == 7)
print(2 == 2)
print(2+3 == 5)
print(3 != 2)
print(not(3 == 2))

print((3>0) and (5>2))
print((3>0) & (5>2))
print((3>5) or (5>2))
print((3>5) | (5>2))

print(5>4>3)
print(2>1>3)

number = 2
print(number)
number += 5
print(number)
number -= 1
print(number)
number *= 2
print(number)
number /= 3
print(number)
number %= 3
print(number)


#숫자처리함수
print(abs(-3))   #절대값
print(pow(4,2))   #거듭제곱근
print(max(3,5,7))   #최댓값
print(min(3,5,9))   #최솟값
print(round(3.49))   #반올림
print(round(3.50))   

from math import *   #math라이브러리 활용
print(floor(3.99))   #반올림
print(ceil(3.01))   #반올림
print(sqrt(4))   #반올림
print(pi)


#랜덤함수
from random import *
print(random())   #0.0~1.0 임의의 값 생성
print(random()*10)
print(int(random()*10))
print(int(random()*45)+1)   #1~45
print(randrange(1,45))   #1이상 45미만
print(randint(1,45))   #1이상 45이하


#문자열
sentence = '문자열'
print(sentence)
sentence = "문자열이지"
print(sentence)
sentence = """
무엇인가
긴
문자열
특,수.문/자?도(시)험-해_보+는#중$이%라@구!요^₩
"""
print(sentence)


#슬라이싱
jumin = "920910-1122334"
print("성별: "+jumin[7])
print("연: "+jumin[0:2])   #0부터 2직전까지
print("월: "+jumin[2:4])
print("일: "+jumin[4:6])
print("생년월일: "+jumin[:6])   #처음부터 6직전까지
print("시크릿 뒷자리: "+jumin[7:])   #7부터 끝까지
print("뒤 7자리(뒤에부터): "+jumin[-7:])   #뒤부터 7글자 (순서가 바뀌지는 않음)


#문자열처리함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())   #이 위치에 있는 글자가 대문자입니까?
print(len(python))   #문자열의 길이
print(python.replace("Python","Java"))
index = python.index("n")   #글자의 위치(문자열도 됨)
print(index)
index = python.index("n",index+1)   #같은 글자의 두 번 째 글자 위치
print(index)
print(python.find("zi"))   #글자가 없으면 -1 (index는 에러가 나는 반면에)
print(python.count("i"))   #글자 등장 횟수(대소문자 구별)


#문자열포맷
print("a" + "b")
print("a","b")

print("나는 %d살이다"%20)
print("나는 %s다"%"새로움을 추구하는 개발자")
print("Apple은 %c로 시작한다"%"A")
print("나는 %s살이다"%20)
print("나는 %s색과 %s색을 좋아한다"%("흰","검정"))

print("나는 {}살이다".format(29))
print("나는 {}색과 {}색을 좋아한다".format("흰","검정"))
print("나는 {1}색과 {0}색을 좋아한다".format("흰","검정"))

print("나는 {age}살이며, {color}색을 좋아한다".format(color="흰", age=29))
 
age = 29
color = "흰"
print(f"나는 {age}살이며, {color}색을 좋아한다") 


#탈출문자
print("백문이 불여일타\n인정?")   #\n : 줄바꿈
print("나는 \"새 개발자\"다")
print("나는 \'새 개발자\'다")
print("역\\슬래쉬\\를 써\\보자\\r이\\나오면\\성공")
print("Red Apple\rPine")   #\r : 커서를 맨 앞으로 이동
print("Red Apple\bPine")   #\b : 백스페이스(한 글자 삭제)
print("Red Apple\tPine")   #\t : 탭


#리스트
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)
subway.append("하동훈")   #항목 추가
print(subway)
subway.insert(1, "정형돈")   #원하는 자리에 항목 추가
print(subway)

print(subway.pop())   #뒤에서부터 하나씩 빼기
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)

subway.append("유재석")
print(subway)
print(subway.count("유재석"))   #해당 문자열과 같은 내용의 항목이 몇 개 있는지 확인

nums = [4,2,5,1,3]
nums.sort()   #순서 오름차순 정렬
print(nums)
nums.reverse()   #순서 뒤집기
print(nums)
nums.clear()   #모두 지우기
print(nums)

mixList = ["조세호", 20, True]   #다향한 자료형 함께 사용 가능
print(mixList)
nums = [6, 7, 8, 9, 0]
nums.extend(mixList)   #리스트 합치기
print(nums)


#사전
IC = {1:"유재석", 2:"박명수", 3:"정준하", 4:"정형돈", 5:"하하", 6:"노홍철", 7:"길"}
print(IC[5])
print(IC.get(7))
print(IC.get(8))   #없는 값을 넣으면 None(그냥 []로 쓰면 에러가 나는 반면에)
print(IC.get(8, "조세호"))   #임의로 끼워넣기
print(IC)
print(3 in IC)   #해당 키값에 value가 있는가?

members = {"1-q":3, "i-3":101, "9-r":23}   #문자열 키 가능
print(members["1-q"])
members["1-q"] = 15   #해당 키값의 재정의
print(members)
del members["i-3"]   #해당 값 삭제
print(members)

print(members.keys())   #key값만 출력
print(members.values())   #value값만 출력
print(members.items())   #둘 다 출력

members.clear()   #모두 지우기
print(members)


#튜플
#리스트와 비슷하나 내용 변경이나 추가 불가 but 속도가 빠름
menu = ("짜장면", "짬뽕")
print(menu[0])
print(menu[1])

(name, age, job) = ("CaCaO", 29, "Developer")
print(name, age, job)


#세트
#중복 안됨, 순서 없음
anyset = {2,3,1,2,3,1,3,3}
print(anyset)

java = {"유재석", "김태호", "조세호"}
python = set(["유재석", "박명수"])
print(java & python)   #교집합
print(java.intersection(python))   #교집합
print(java | python)   #합집합
print(java.union(python))   #합집합
print(java - python)   #차집합
print(java.difference(python))   #차집합

java.remove("김태호")   #세트에서 하나 빼기
print(java)


#자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))
menu = list(menu)
print(menu, type(menu))
menu = tuple(menu)
print(menu, type(menu))
menu = set(menu)
print(menu, type(menu))























