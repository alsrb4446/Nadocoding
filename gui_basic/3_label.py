from tkinter import * # import tkinter 하면 tkinter.Tk()식으로 써야함.

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="gui_basic/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")

    global photo2   #garbage collection 때문에 함수내에서 이미지 바꾸려면 전역변수 선언해줘야함
    photo2 = PhotoImage(file="gui_basic/img2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command = change)
btn.pack()

root.mainloop()