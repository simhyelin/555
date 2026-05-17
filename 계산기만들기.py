import tkinter as tk

def add():
    result = int(entry1.get()) + int(entry2.get())
    label.config(text=f"Result: {result}")

root = tk.Tk()
entry1 = tk.Entry(root)
entry1.pack()
entry2 = tk.Entry(root)
entry2.pack()
button = tk.Button(root, text="Add", command = add)
button.pack()
label = tk.Label(root,text="")
label.pack()
root.mainloop()
