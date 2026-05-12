'''
from tkinter import *
window = Tk()

photo = PhotoImage(file = "img.gif")
button1 = Button(window, image = photo, command = quit)

button1.pack()

window.mainloop()
'''

'''
from tkinter import *
from tkinter import messagebox

def myFunc() :
    messagebox.showinfo("펭귄 버튼", "팽귄이 귀엽죠?^^")

window = Tk()

photo = PhotoImage(file = "img.gif")
button1 = Button(window, image = photo, command = myFunc)

button1.pack()

window.mainloop()
'''
'''
from tkinter import *
from tkinter import messagebox
window = Tk()

def myFunc() :
    if chk.get() == 0 :
        messagebox.showinfo("","체크버튼이 꺼졌어요.")
    else :
        messagebox.showinfo("","체크버튼이 커졌어요.")

chk = IntVar()
cb1 = Checkbutton(window, text = "클릭하세요", variable = chk, command = myFunc)

cb1.pack()

window.mainloop()
'''

'''
from tkinter import *
from tkinter import messagebox
window = Tk()

def myFunc() :
    if var.get() == 1 :
        label1.configure(text = "파이썬")
    elif var.get() == 2 :
        label1.configure(text = "C++")
    else:
        label1.configure(text = "Java")

var = IntVar()
rb1 = Radiobutton(window, text = "파이썬", variable = var, value = 1, command = myFunc)
rb2 = Radiobutton(window, text = "C++", variable = var, value = 2, command = myFunc)
rb3 = Radiobutton(window, text = "Java", variable = var, value = 3,command = myFunc)

label1 = Label(window, text = "tjsxorgks djsdj:", fg = "red")

rb1.pack()
rb2.pack()
rb3.pack()
label.pack()

window.mainloop()
'''
'''
from tkinter import *

btnList = [None] * 9
fnameList = ["img.gif"]
photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

window = Tk()
window.geometry("600x600")

for i in range(0,9):
    photoList[i] = PhotoImage(file = "img.gif")
    btnList[i] = Button(window, image = photoList[i])

for i in range(0,3):
    for k in range(0,3):
        btnList[num].place(x=xPos, y=yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70

window.mainloop()
'''
from tkinter import *
from tkinter import messagebox

def clickLeft(event):
    messagebox.showinfo("마우스", "마우스 왼쪽 버튼이 클릭됨")

window = Tk()

window.bind("<Button-1>",clickLeft)

window.mainloop()
