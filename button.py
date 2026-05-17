import tkinter as tk

def say_hello():
    name = entry.get()
    label.config(text = 'hello! {}'.format(name))
root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text = "Click Me", command=say_hello)
button.pack()
label = tk.Label(root, text = 'No input')
label.pack()
root.mainloop()
