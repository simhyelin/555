from tkinter import*

class Counter:
    total_clicks = 0

    def __init__(self, start=0):
        self.value = start

    def increment(self):
        self.value += 1
        #pass

    def decrement(self):
        self.value -= 1
        if(self.value < 0):
            self.value = 0
        #pass

    def reset(self):
        self.value += 0
        #pass

    def update_label():
        label.config(text=f"현재 값: {counter.value}")
        #pass

    def on_minus():
        counter.increment()
        update_label()

    def on_reset():
        counter.reset()
        update_label()        
        #pass

counter = Counter(start=0)

root = Tk()
root.title("연습1-Counter 클래스 + GUI")
root.geometry("360x150")

label = Label(root, text="", font=("맑은 고딕", 14))
label.pack(pady=10)

btn_plus  = Button(root, text="+", width=6, command=on_plus)
btn_minus = Button(root, text="-", width=6, command=on_minus)
btn_reset = Button(root,text="Reset", width=8, command=on_reset)

btn_plus.pack(side=LEFT, padx=q0, pady=10)
btn_minus.pack(side=LEFT, padx=10, pady=10)
btn_reset.pack(side=LEFT, padx=10, pady=10)

update_label()
window.mainloop()
