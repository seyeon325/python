import tkinter

# 루트 객체 생성
root = tkinter.Tk()
root.title("12주차 미나")

# 캔버스 생성
canvas = tkinter.Canvas(root, width=800, height=600, bg="skyblue")
canvas.pack()

# 배경 이미지 추가
bgimg = tkinter.PhotoImage(file="mina.png")
canvas.create_image(400, 300, image=bgimg)

# 마우스 위치 표시용 라벨
mouse_label = tkinter.Label(root, text="마우스 위치: ")
mouse_label.pack()

# 마우스 위치 출력 함수
def show_mouse_position(event):
    x = event.x
    y = event.y
    mouse_label["text"] = f"마우스 위치: {x}, {y}"

# 마우스 움직임 이벤트 바인딩
canvas.bind("<Motion>", show_mouse_position)

#
cbtn = tkinter. Checkbutton(text = "체크 버튼")
cbtn.place(x= 100, y=100)

# 메인 루프 실행
root.mainloop()
