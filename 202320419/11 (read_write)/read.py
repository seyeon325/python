import tkinter
root = tkinter.Tk()

root.title("제목")
root.geometry("300x300")

file = open("test.txt", "r", encoding= "UTF -8")

strFile = file.readline()
root.geometry(strFile)

strFile = file.readline()
root.title(strFile[:-1])

file.close()

root.mainloop()