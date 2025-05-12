#test.txt 파일을 읽어와서
#outTest.txt 파일에 작성한다.
inFile = opne("test.txt", "r", encoding="UFT-8")

outfile = open("outTest.txt", "w", encoding="UFT-8")

while True:
    strFile = inFile.readline()
    if(str == ""):
        break
    outfile.writelines(strFile)

inFile.close()
outfile.close()