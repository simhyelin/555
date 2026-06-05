# 염분(PSU) = 소금 질량 / (물 질량 + 소금 질량) × 1000

from tkinter import *
from tkinter import messagebox

## 클래스 선언 부분 ##
class Salinity:
    def __init__(self, water_g, salt_g):
        if water_g <= 0 or salt_g < 0:
            raise ValueError("물은 0보다 커야 하고, 소금은 0 이상이어야 합니다.")
        self.water_g = water_g
        self.salt_g  = salt_g

    def psu(self):
        """염분 농도 [PSU = g/kg]"""
        return self.salt_g / (self.water_g + self.salt_g) * 1000

    def category(self):
        """수괴 분류"""
        p = self.psu()
        if p < 0.5:
            return "담수 (Fresh Water)"
        elif p < 5:
            return "기수 (Brackish Water)"
        elif p < 30:
            return "저염수"
        elif p <= 40:
            return "정상 해수 (Normal Seawater)"
        else:
            return "고염수 (Hypersaline)"

## 함수 선언 부분 ##
def on_calc():
    try:
        water = float(e_water.get())
        salt  = float(e_salt.get())
        s = Salinity(water, salt)
    except ValueError:
        messagebox.showerror("입력 오류", "숫자로 입력해 주세요.")
        return

    result_label.config(text=f"염분 농도 = {s.psu():.2f} PSU\n분류: {s.category()}")

## 메인 코드 부분 ##
window = Tk()
window.title("염분 계산기")
window.geometry("380x200")

# 입력칸: 물
Label(window, text="물의 양 [g]:").grid(row=0, column=0, sticky="e", padx=8, pady=8)
e_water = Entry(window, width=12)
e_water.grid(row=0, column=1, padx=8, pady=8)
e_water.insert(0, "1000")

# 입력칸: 소금
Label(window, text="소금의 양 [g]:").grid(row=1, column=0, sticky="e", padx=8, pady=8)
e_salt = Entry(window, width=12)
e_salt.grid(row=1, column=1, padx=8, pady=8)
e_salt.insert(0, "35")

Button(window, text="계산", width=12, command=on_calc).grid(row=2, column=0, columnspan=2, pady=10)

result_label = Label(window, text="", font=("Consolas", 12), justify=LEFT)
result_label.grid(row=3, column=0, columnspan=2)

window.mainloop()
