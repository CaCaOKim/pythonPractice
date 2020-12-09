from random import *
total = 0

for i in range(1,51):
    time = randint(1, 50)
    OX = " "
    
    if time in range(5,16):
        OX = "O"
        total += 1

    print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(OX, i, time))

print("총 탑승 승객: {}분".format(total))













