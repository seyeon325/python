import tkinter

# 루트 객체 생성
root = tkinter.Tk()
root.title("첫 번째 캔버스")

# 캔버스 생성
canvas = tkinter.Canvas(root, width=400, height=600, bg="skyblue")
canvas.pack()

# 캔버스 내 이미지 생성
gazou = tkinter.PhotoImage(file="miko.png")
canvas.create_image(200, 300, image=gazou)

# 메인 루프 실행
root.mainloop()


#루트 -> 캔버스 -> 백그라운드z