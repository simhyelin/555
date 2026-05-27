from tkinter import *
from tkinter import messagebox

G = 9.81


## 클래스 선언 부분 ##
class Particle:
    def __init__(self, radius_um, rho_p=2650.0, rho_f=1025.0, mu=1.07e-3):
        self.r = radius_um * 1e-6     # µm → m
        self.rho_p = rho_p
        self.rho_f = rho_f
        self.mu = mu

    def settling_velocity(self):
        """침강속도 w [m/s]"""
        # TODO: (2/9)*(rho_p - rho_f)*g*r² / mu 반환
        return (2/9)*(self.rho_p - self.rho_f)*9.81*self.r**2/self.mu

    def reynolds(self):
        """레이놀즈수 Re (무차원)"""
        w = self.settling_velocity()
        # TODO: rho_f * w * (2r) / mu 반환 (w 가 음수면 절댓값 사용)
        if w <= 0:
            return abs(w)
        
        return self.rho_f * w * (2*self.r) / self.mu
        

    def stokes_valid(self):
        return self.reynolds() < 0.5


## 함수 선언 부분 ##
def on_calc():
    try:
        r  = float(e_r.get())
        rp = float(e_rp.get())
        rf = float(e_rf.get())
    except ValueError:
        messagebox.showerror("입력 오류", "숫자로 입력해 주세요.")
        return

    p = Particle(r, rho_p=rp, rho_f=rf)
    w  = p.settling_velocity()
    re = p.reynolds()
    valid = "유효 (층류)" if p.stokes_valid() else "주의: Re가 커서 과대평가될 수 있음"
    result.config(text=(f"침강속도 w = {w*1000:.4f} mm/s  ({w:.3e} m/s)\n"
                        f"Reynolds Re = {re:.4f}\n"
                        f"Stokes 유효성: {valid}"))


## 메인 코드 부분 ##
window = Tk()
window.title("연습 13 - 입자 침강속도 (Stokes)")
window.geometry("430x250")

rows = [("입자 반경 [µm]:", "10"), ("입자 밀도 ρp [kg/m³]:", "2650"),
        ("해수 밀도 ρf [kg/m³]:", "1025")]
entries = []
for i, (lab, dv) in enumerate(rows):
    Label(window, text=lab).grid(row=i, column=0, sticky="e", padx=8, pady=6)
    e = Entry(window, width=12); e.grid(row=i, column=1, padx=8, pady=6)
    e.insert(0, dv); entries.append(e)
e_r, e_rp, e_rf = entries

Button(window, text="계산", width=12, command=on_calc).grid(row=3, column=0, columnspan=2, pady=10)
result = Label(window, text="", font=("Consolas", 10), justify=LEFT)
result.grid(row=4, column=0, columnspan=2)

window.mainloop()
