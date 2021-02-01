from tkinter import * # import tkinter 하면 tkinter.Tk()식으로 써야함.


root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

txt = Text(root, width=30,height=5) # 엔터 가능
txt.pack()
txt.insert(END,"글자를 입력하세요")


e = Entry(root, width=30) # 한줄로만 입력가능, id or password 등
e.pack()
e.insert(0,"한 줄만 입력해요") # 현재 값이 비어있으므로 END를 써도 무방

def btncmd():
    #내용 출력
    print(txt.get("1.0", END)) # 라인 1부터 가져와라, COLUMN기준으로 0번째부터 END까지
    print(e.get())

    #내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()