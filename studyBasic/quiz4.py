from random import *

IDs = list(range(1,21))
print("-- 당첨자 발표 --")
shuffle(IDs)
print("치킨 당첨자: "+str(IDs.pop()))
print("커피 당첨자: "+str(sample(IDs, 3)))
print("-- 축하합니다 --")
