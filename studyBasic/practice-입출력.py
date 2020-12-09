#표준입출력
print("Python", "Java", "JavaScript", sep=" vs ", end="?")   #sep: 입력값 구분, end:맨 끝에 뭐가 오는가? 라인개행 없음
print("무엇이 더 재미있을까요?")

import sys
print("Python", "Java", file=sys.stdout)   #표준 출력
print("Python", "Java", file=sys.stderr)   #표준 에러

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8),  str(score).rjust(4), sep=":")   #ljust(n): 왼쪽 정렬 후 n칸 띄우기, rjust(n): n칸 띄운 후 오른쪽 정렬

for num in range(1,21):
    print("대기번호 : "+ str(num).zfill(3))   #3칸의 값을 집어넣으나 빈자리는 0으로 채움

# answer = input("아무 값이나 입력하세요 : ")   #input으로 입력한 값은 항상 문자열type
# print("입력하신 값은 "+answer+"입니다")


#다양한 출력포맷
print("{0: >10}".format(500))   #총 10자리 확보하고 오른쪽정렬을 한다. 빈 자리는 빈 공간으로
print("{0: >+10}".format(500))   #부호 표시
print("{0: >+10}".format(-500))
print("{0:_>10}".format(500))   #왼쪽정렬을 하고 빈 자리는 _으로
print("{0:,}".format(100000000000))   #세자리 마다 ,찍어주기
print("{0:+,}".format(100000000000))   #세자리 마다 ,찍어주면서 부호 붙이기
print("{0:+,}".format(-100000000000))
print("{0:^<+30,}".format(100000000000))   #30칸을 확보하여 빈자리는 ^으로 채우고 부호를 붙이며 세자리마다 ,찍기
print("{0:f}".format(5/3))   #소수 출력
print("{0:2f}".format(5/3))   #소수점 둘 째 자리까지 출력   셋 째 자리에서 반올림


#파일입출력
# score_file = open("score.txt", "w", encoding="utf8")   #w: 읽기 전용
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")   #a: append 내용 추가하기
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")   #r: 읽기 전용
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline())   #줄별로 읽기, 한줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:   #라인이 총 몇 줄인지 모를 때 while을 이용
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()   #list형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()


#pickle
import pickle
# profile_file = open("profile.pickle", "wb")   #wb: 바이너리 타입, 피클은 항상 바이너리타입으로 해줘야 함
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)   #profile에 있는 정보를 file에 저장
# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)   #file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()


#with
with open("profile.pickle", "rb") as profile_file:   #profile_file이라는 변수에 저장
    print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())



