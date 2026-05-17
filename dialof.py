from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.geometry("400x100")

Label = Label(root, text = "demo3.gif")
Label.pack()

filename = askopenfilename(parent = root, filetypes = (("GIF파일", "gif"),("모든파일", "*.*")))

Label.configure(text = str(filename))

root.mainloop
