from tkinter import *
from tkinter import messagebox
from tkinter import ttk

RHO, G = 1025.0, 9.81


## 클래스 선언 부분 ##
class UnitConverter:
    # 변환 이름: (변환함수, 입력단위표시, 출력단위표시)
    CONVERSIONS = {
        "노트 → m/s":      (lambda x: x * 0.514444,            "knot", "m/s"),
        "m/s → 노트":      (lambda x: x / 0.514444,            "m/s",  "knot"),
        "섭씨 → 화씨":     (lambda x: x * 9/5 + 32,            "°C",   "°F"),
        "화씨 → 섭씨":     (lambda x: (x - 32) * 5/9,          "°F",   "°C"),
        "해리 → km":       (lambda x: x * 1.852,               "nm",   "km"),
        "km → 해리":       (lambda x: x / 1.852,               "km",   "nm"),
        "dbar → 수심(m)":  (lambda x: x * 10000 / (RHO * G),   "dbar", "m"),
        "수심(m) → dbar":  (lambda x: x * RHO * G / 10000,     "m",    "dbar"),
    }

    def names(self):
        return list(self.CONVERSIONS.keys())

    def convert(self, kind, value):
        """kind(문자열)에 해당하는 변환을 value 에 적용해 (결과, 입력단위, 출력단위) 반환"""
        # TODO: CONVERSIONS[kind] 에서 (func, u_in, u_out) 꺼내기
        # TODO: func(value) 로 결과 계산해서 (결과, u_in, u_out) 반환
        func, u_in, u_out = self.CONVERSIONS[kind]
        return func(value), u_in, u_out


## 함수 선언 부분 ##
conv = UnitConverter()


def on_convert():
    kind = combo.get()
    try:
        v = float(entry.get())
    except ValueError:
        messagebox.showerror("입력 오류", "변환할 값을 숫자로 입력해 주세요.")
        return
    result_val, u_in, u_out = conv.convert(kind, v)
    result.config(text=f"{v:g} {u_in}  =  {result_val:.4f} {u_out}")


## 메인 코드 부분 ##
window = Tk()
window.title("연습 16 - 해양 단위 변환기")
window.geometry("420x200")

Label(window, text="변환 종류:").grid(row=0, column=0, padx=8, pady=10, sticky="e")
combo = ttk.Combobox(window, values=conv.names(), state="readonly", width=18)
combo.grid(row=0, column=1, padx=8, pady=10)
combo.current(0)

Label(window, text="값:").grid(row=1, column=0, padx=8, pady=6, sticky="e")
entry = Entry(window, width=20); entry.grid(row=1, column=1, padx=8, pady=6)
entry.insert(0, "10")

Button(window, text="변환", width=12, command=on_convert).grid(row=2, column=0, columnspan=2, pady=10)
result = Label(window, text="", font=("Consolas", 13))
result.grid(row=3, column=0, columnspan=2)

window.mainloop()
