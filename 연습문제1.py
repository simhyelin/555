from tkinter import*

class Counter:
    total_clicks = 0  

    def __init__(self, start=0):
        self.value = start   

    def increment(self):
        self.value += 1
        Counter.total_clicks += 1

    def decrement(self):
        self.value -= 1
        Counter.total_clicks += 1

    def reset(self):
        self.value = 0

def update_label():
    label.config(text=f"현재 값: {counter.value}   /   총 클릭수: {Counter.total_clicks}")


def on_plus():
    counter.increment()
    update_label()


def on_minus():
    counter.decrement()
    update_label()


def on_reset():
    counter.reset()
    update_label()


counter = Counter(start=0)

window = Tk()
window.title("연습 1 - Counter 클래스 + GUI")
window.geometry("360x150")

label = Label(window, text="", font=("맑은 고딕", 14))
label.pack(pady=10)

btn_plus  = Button(window, text="+",   width=6, command=on_plus)
btn_minus = Button(window, text="-",   width=6, command=on_minus)
btn_reset = Button(window, text="Reset", width=8, command=on_reset)

btn_plus.pack(side=LEFT,  padx=10, pady=10)
btn_minus.pack(side=LEFT, padx=10, pady=10)
btn_reset.pack(side=LEFT, padx=10, pady=10)

update_label()
window.mainloop()
