#test.txt 파일을 읽어와서
#outTest.txt 파일에 작성한다.
inFile = opne("test.txt", "r", encoding="UFT-8")

outfile = open("outTest.txt", "w", encoding="UFT-8")

# 파일 읽어서 쓰기
while True:
    strFile = inFile.readline()
    if(str == ""):
    for ch in strFile:
        #암호화
        chNum = ord(ch)
        chNum = chNum + 100
        chChange =chr(chNum)
 #기록
        strFileChange += chChange
        break
    outfile.writelines(strFileChange)

inFile.close()
outfile.close()