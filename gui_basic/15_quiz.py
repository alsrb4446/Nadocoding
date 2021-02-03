import os
from tkinter import * # import tkinter 하면 tkinter.Tk()식으로 써야함.

root = Tk()
root.title("제목없음 - Windows 메모장")
root.geometry("640x480")

menu = Menu(root)

filename= "mynote.txt"

def file_open():
    if os.path.isfile(filename): #파일 있으면 true, 없으면 false
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END) # 텍스트 위젯 본문 삭제
            txt.insert(END, file.read()) # 파일 내용을 본문에 입력

def file_save():
    with open(filename, "w", encoding="utf8") as file:
         file.write(txt.get("1.0", END))
    

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=file_open)
menu_file.add_command(label="저장", command=file_save)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

#스크롤바
scrollbar =Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# 텍스트
txt = Text(root, yscrollcommand=scrollbar.set) # 엔터 가능
txt.pack(side = "left",fill="both", expand=True)
scrollbar.config(command=txt.yview)

root.config(menu=menu)
root.mainloop()