from tkinter import *
import math


## 클래스 선언 부분 ##
class Constituent:
    def __init__(self, name, amplitude, period_hr, phase_deg=0.0):
        self.name = name
        self.A = amplitude
        self.T = period_hr
        self.phi = math.radians(phase_deg)

    def eta(self, t):
        return self.A * math.cos(2 * math.pi * t / self.T - self.phi)


class Tide:
    def __init__(self, constituents, mean_level=0.0):
        self.constituents = constituents
        self.mean_level = mean_level

    def eta(self, t):
        return self.mean_level + sum(c.eta(t) for c in self.constituents)

    def extrema(self, t0, t1, dt=0.02):
        result = []
        prev = self.eta(t0)
        cur = self.eta(t0 + dt)
        t = t0 + dt
        while t < t1:
            nxt = self.eta(t + dt)
            if prev < cur > nxt:
                result.append((t, cur, "고조"))
            elif prev > cur < nxt:
                result.append((t, cur, "저조"))
            prev, cur = cur, nxt
            t += dt
        return result


## 함수 선언 부분 ##
tide = Tide([
    Constituent("M2", 0.80, 12.4206,  0),
    Constituent("S2", 0.30, 12.0000, 30),
    Constituent("K1", 0.25, 23.9345, 60),
    Constituent("O1", 0.18, 25.8193, 90),
], mean_level=1.5)


def hhmm(t):
    h = int(t) % 24
    m = int(round((t - int(t)) * 60))
    if m == 60:
        h = (h + 1) % 24
        m = 0
    return f"{h:02d}:{m:02d}"


def on_predict():
    text.delete("1.0", END)
    text.insert(END, f"{'시각':>6}   {'구분':>4}   {'조위(m)':>8}\n")
    text.insert(END, "-" * 28 + "\n")
    for t, eta, kind in tide.extrema(0, 24):
        text.insert(END, f"{hhmm(t):>6}   {kind:>4}   {eta:8.3f}\n")


## 메인 코드 부분 ##
window = Tk()
window.title("연습 17 - 조석 고조·저조 예보표 (향후 24시간)")
window.geometry("360x420")

Button(window, text="24시간 예보 생성", command=on_predict).pack(pady=8)

text = Text(window, font=("Consolas", 12), width=30)
text.pack(fill=BOTH, expand=True, padx=10, pady=8)

on_predict()
window.mainloop()

