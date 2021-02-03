from tkinter import * # import tkinter 하면 tkinter.Tk()식으로 써야함.

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand= scrollbar.set)
for i in range(1,32):
    listbox.insert(END, str(i)+"일")
listbox.pack(side="left")

scrollbar.config(command=listbox.yview) #scrollbar 와 listbox 연동

root.mainloop()