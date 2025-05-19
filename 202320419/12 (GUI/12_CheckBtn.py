# 체크박스 + 메시지박스 예제

import tkinter
import tkinter.messagebox  # 메시지박스 사용
import random

# 루트 객체 생성
root = tkinter.Tk()
root.title("12주차 미나")  # 윈도우 타이틀 설정

# 체크 버튼 클릭 시 동작할 함수
def chkbtnClick():
    # 체크 버튼이 체크되었는지 확인
    if cvalue.get() == True:
        print("체크 되었습니다")  # 체크되었을 때 출력

        # 메시지 박스 예시 (필요 시 주석 해제해서 확인 가능)

        # tkinter.messagebox.showinfo("체크박스", "체크박스가 선택되었습니다!")
        # tkinter.messagebox.showwarning("경고", "주의가 필요합니다.")
        # tkinter.messagebox.showerror("오류", "문제가 발생했습니다.")
        # Yes/No 질문
        #answer = tkinter.messagebox.askyesno("체크박스", "동의하시겠습니까?")
        if answer:
            print("동의")
        else:
            print("거절")
    else:
        print("체크가 해제 되었습니다.")  # 체크 해제되었을 때 출력
        tkinter.messagebox.showwarning("체크박스", "체크박스가 해제되었습니다.")

# 캔버스 생성
canvas = tkinter.Canvas(root, width=800, height=600, bg="skyblue")  # 배경색 skyblue로 설정
canvas.pack()

# 배경 이미지 추가
bgimg = tkinter.PhotoImage(file="mina.png")  # 이미지 로드
canvas.create_image(400, 300, image=bgimg)  # 캔버스 중앙에 이미지 삽입

# 마우스 위치 라벨
mouse_label = tkinter.Label(root, text="마우스 위치: ")
mouse_label.pack()

# 마우스 위치 출력 함수
def show_mouse_position(event):
    x = event.x
    y = event.y
    mouse_label["text"] = f"마우스 위치: {x}, {y}"

# 마우스 움직임 이벤트 바인딩
canvas.bind("<Motion>", show_mouse_position)

# 체크버튼 상태 변수
cvalue = tkinter.BooleanVar()
cvalue.set(False)  # 기본값: 체크되지 않음

# 체크버튼 생성
cbtn = tkinter.Checkbutton(text="체크 버튼", variable=cvalue, command=chkbtnClick)
cbtn.place(x=100, y=100)

# 메인 루프 실행
root.mainloop()
