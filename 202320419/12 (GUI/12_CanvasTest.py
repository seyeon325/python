import tkinter
import random

# 루트 객체 생성
root = tkinter.Tk()
root.title("첫 번째 캔버스")

# 캔버스 생성
canvas = tkinter.Canvas(root, width=800, height=600, bg="skyblue")
canvas.pack()

# 배경 이미지 추가
bgimg = tkinter.PhotoImage(file="miko.png")
canvas.create_image(400, 300, image=bgimg)

# 마우스 위치 표시용 라벨
mouse_label = tkinter.Label(root, text="마우스 위치: ")
mouse_label.pack()

# 제비뽑기 결과 라벨 (크게, 버튼 위에 표시)
label = tkinter.Label(root, text="", font=("맑은 고딕", 36), fg="blue", bg="skyblue")
label.place(x=150, y=380)  # 버튼 위 위치 조정

# 결과 기록용 텍스트 박스
text = tkinter.Text(root, height=5)
text.pack()

# 마우스 위치 출력 함수
def show_mouse_position(event):
    x = event.x
    y = event.y
    mouse_label["text"] = f"마우스 위치: {x}, {y}"

canvas.bind("<Motion>", show_mouse_position)

# 버튼 클릭 시 제비뽑기 함수
def click_btn():
    result = random.choice(["대길", "중길", "소길", "흉"])
    label["text"] = result
    text.insert(tkinter.END, result + "\n")

# 사각형 버튼 배경 (캔버스)
canvas.create_rectangle(100, 450, 300, 520, fill="darkgray", outline='red', width=5)

# 버튼 위에 배치
button = tkinter.Button(root, text="제비뽑기", font=("맑은 고딕", 24), command=click_btn)
button.place(x=500, y=400)

# 메인 루프 실행
root.mainloop()
