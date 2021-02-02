import tkinter.ttk as ttk   
from tkinter import * # import tkinter 하면 tkinter.Tk()식으로 써야함.


root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

values = [str(i)+"일" for i in range(1,32)] # 1부터 31까지의 숫자
combobox = ttk.Combobox(root, height = 5, values=values)
combobox.set("카드 결제일") #최초 목록 제목 설정
combobox.pack()

combobox2 = ttk.Combobox(root, height = 10, values=values, state="readonly")
combobox2.current(0) # 0번째 인덱스 값 선택
combobox2.pack()


def btncmd():
    print(combobox.get()) # 선택된 값 표시
    print(combobox2.get()) # 선택된 값 표시

btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()