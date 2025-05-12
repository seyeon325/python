outfile = open("outTest.txt", "w",encoding="UTF-8")

while True:
    outStr = input("내용 입력 ==> ")

    if outStr == '끝':
        break
    outfile.writelines(outStr+"\n")




outfile.close()
