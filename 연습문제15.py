from tkinter import *
from tkinter import messagebox


def density(T, S):
    """EOS-80 (P=0) 해수 밀도 [kg/m³]"""
    rho_w = (999.842594 + 6.793952e-2*T - 9.095290e-3*T**2
             + 1.001685e-4*T**3 - 1.120083e-6*T**4 + 6.536336e-9*T**5)
    A = (8.24493e-1 - 4.0899e-3*T + 7.6438e-5*T**2 - 8.2467e-7*T**3 + 5.3875e-9*T**4)
    B = (-5.72466e-3 + 1.0227e-4*T - 1.6546e-6*T**2)
    C = 4.8314e-4
    return rho_w + A*S + B*S**1.5 + C*S*S


## 클래스 선언 부분 ##
class WaterSample:
    def __init__(self, T, S, label=""):
        self.T = T
        self.S = S
        self.label = label

    def density(self):
        # TODO: 위 density(T, S) 함수를 사용해 밀도 반환
        return density(self.T, self.S)

    def sigma_t(self):
        # TODO: density() - 1000 반환
        return density() - 1000 #density(self.T, self.S)도 가능

## 화면 범위 (필요시 수정) ##
S_MIN, S_MAX = 32.0, 35.5
T_MIN, T_MAX = 0.0, 28.0
PAD = 50

samples = [
    WaterSample(24.0, 33.8, "표층수"),
    WaterSample(15.0, 34.3, "중층수"),
    WaterSample(2.0,  34.6, "심층수"),
]


## 함수 선언 부분 ##
def to_px(S, T, W, H):
    x = PAD + (S - S_MIN) / (S_MAX - S_MIN) * (W - 2*PAD)
    y = (H - PAD) - (T - T_MIN) / (T_MAX - T_MIN) * (H - 2*PAD)   # T 위로
    return x, y


def find_T_for_sigma(target, S):
    """고정 S 에서 σ_t = target 을 주는 T 를 이분법으로 탐색 (없으면 None)"""
    lo, hi = T_MIN, T_MAX
    f = lambda T: (density(T, S) - 1000) - target
    if f(lo) * f(hi) > 0:
        return None              # 구간 내 해 없음
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def draw():
    canvas.delete("all")
    W = canvas.winfo_width(); H = canvas.winfo_height()
    if W < 60 or H < 60:
        return

    # 외곽 + 축
    canvas.create_rectangle(PAD, PAD, W-PAD, H-PAD, outline="black")
    canvas.create_text(W/2, H-15, text="염분 S [PSU]", font=("맑은 고딕", 10))
    canvas.create_text(16, H/2, text="수온 T [°C]", angle=90, font=("맑은 고딕", 10))

    # 등밀도선 (σ_t = 20,21,...,28)
    for sigma in range(20, 29):
        pts = []
        steps = 60
        for i in range(steps + 1):
            S = S_MIN + (S_MAX - S_MIN) * i / steps
            T = find_T_for_sigma(sigma, S)
            if T is not None:
                pts.append(to_px(S, T, W, H))
        for (x1, y1), (x2, y2) in zip(pts[:-1], pts[1:]):
            canvas.create_line(x1, y1, x2, y2, fill="#cfcfcf")
        if pts:
            canvas.create_text(pts[-1][0]-6, pts[-1][1], text=f"{sigma}",
                               fill="#999999", font=("Consolas", 8))

    # 관측점 (TODO 영역)
    for smp in samples:
        x, y = to_px(smp.S, smp.T, W, H)
        # TODO: 점 그리기 (create_oval) + 라벨(create_text) + σ_t 값 표시
        canvas.create_oval(x-4, y-4, x+4, y+4, fill="red", outline="") + canvas.create_text(x+8, y, anchor="w", text=f"{smp.label} (σt={smp.sigma_t():.2f})",font=("맑은 고딕", 9))



def on_add():
    try:
        T = float(e_T.get()); S = float(e_S.get())
        lab = e_lab.get().strip()
    except ValueError:
        messagebox.showerror("입력 오류", "T, S 는 숫자로 입력해 주세요.")
        return
    samples.append(WaterSample(T, S, lab))
    draw()


## 메인 코드 부분 ##
window = Tk()
window.title("연습 15 - T-S 다이어그램")
window.geometry("560x520")

top = Frame(window); top.pack(fill=X, pady=6)
Label(top, text="T:").pack(side=LEFT)
e_T = Entry(top, width=6); e_T.pack(side=LEFT, padx=2); e_T.insert(0, "10.0")
Label(top, text="S:").pack(side=LEFT)
e_S = Entry(top, width=6); e_S.pack(side=LEFT, padx=2); e_S.insert(0, "34.0")
Label(top, text="라벨:").pack(side=LEFT)
e_lab = Entry(top, width=8); e_lab.pack(side=LEFT, padx=2); e_lab.insert(0, "신규")
Button(top, text="점 추가", command=on_add).pack(side=LEFT, padx=8)

canvas = Canvas(window, bg="white")
canvas.pack(fill=BOTH, expand=True, padx=10, pady=8)
canvas.bind("<Configure>", lambda e: draw())

window.mainloop()
