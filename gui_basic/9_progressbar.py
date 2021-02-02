import time
import tkinter.ttk as ttk   
from tkinter import * # import tkinter 하면 tkinter.Tk()식으로 써야함.


root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# progressbar = ttk.Progressbar(root, maximum=100, mode = "indeterminate")
# progressbar.start(10) # 10ms마다 움직임
# progressbar.pack()

# progressbar2 = ttk.Progressbar(root, maximum=100, mode = "determinate")
# progressbar2.start(10) # 10ms마다 움직임
# progressbar2.pack()

# def btncmd():
#     progressbar.stop()
#     progressbar2.stop()

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var3 = DoubleVar()
progressbar3 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var3)
progressbar3.pack()

def btncmd2():
    for i in range(101):
        time.sleep(0.01) # 0.01초 대기
        
        p_var3.set(i) # progress bar의 값 설정
        progressbar3.update() # ui 업데이트
        print(p_var3.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()