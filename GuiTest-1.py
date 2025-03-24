import tkinter #tkinter 실행
import tkinter.font

root = tkinter.Tk ()

root.title("첫 번째 윈도우") #윈도우 창 이름
root.geometry("800x600")   #해상도

labelA = tkinter.Label(root, text="동", font=("system", 24)) #라벨 만들기
labelA.place(x=600, y=300) #대치 시킨다

labelB = tkinter.Label(root, text="서", font=("system", 24)) #라벨 만들기
labelB.place(x=200, y=300) #대치 시킨다

labelC = tkinter.Label(root, text="남", font=("system", 24)) #라벨 만들기
labelC.place(x=400, y=500) #대치 시킨다

labelD = tkinter.Label(root, text="북", font=("system", 24)) #라벨 만들기
labelD.place(x=400, y=100) #대치 시킨다

#labelA.place(x=300,y=300)

btn = tkinter.Button(root, text="버튼", font=("system, 10")) #버튼 만들기
btn.place(x=400, y= 300,width=30, height=30) #버튼 대치

entry = tkinter.Entry(width=5)
entry.place(x=200, y=350)

print(tkinter.font.families()) 


root.mainloop() #루프


#텍스트 입력