for cnt in range(1,51):
    with open(str(cnt)+"주차.txt", "w", encoding="utf8") as WR:
        WR.write("- {} 주차 주간 보고 -".format(cnt))
        WR.write("\n부서 : ")
        WR.write("\n이름 : ")
        WR.write("\n업무 요약 : ")
