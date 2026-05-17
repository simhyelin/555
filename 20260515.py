from tkinter import *

root = Tk()

mainMenu = Menu(root)
root.config(menu = mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "열기")
fileMenu.add_separator()
fileMenu.add_command(label = "종류")

root.mainloop()


from tkinter import *
from tkinter import messagebox

def func_open():
    messagebox.showinfo("메뉴선택", "열기 메뉴를 선택함")

def func_exit():
    root.quit()
    root.destroy()
    
root = Tk()

mainMenu = Menu(root)
root.config(menu = mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "열기")
fileMenu.add_separator()
fileMenu.add_command(label = "종류")

root.mainloop()

