from tkinter import *
from tkinter import messagebox


## 클래스 선언 부분 ##
class Station:
    def __init__(self, name, lat, lon, depth):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.depth = depth      # 수심 [m]

    def __lt__(self, other):
        # TODO: 수심(depth) 기준 정렬을 위해 self.depth < other.depth 반환
        return self.depth < other.depth

    def __eq__(self, other):
        # TODO: 이름이 같으면 같은 정점으로 간주
        return self.depth == self.other

    def __repr__(self):
        return f"{self.name} ({self.lat:.2f}, {self.lon:.2f})  수심 {self.depth:.0f} m"


## 함수 선언 부분 ##
stations = [
    Station("ST-A", 35.10, 129.10, 120),
    Station("ST-B", 34.80, 128.50,  45),
    Station("ST-C", 35.40, 129.60, 350),
]


def refresh_listbox():
    listbox.delete(0, END)
    for st in stations:
        listbox.insert(END, repr(st))


def on_add():
    try:
        name = e_name.get().strip()
        if not name:
            raise ValueError("이름을 입력하세요.")
        lat = float(e_lat.get())
        lon = float(e_lon.get())
        dep = float(e_dep.get())
    except ValueError as ex:
        messagebox.showerror("입력 오류", str(ex))
        return
    stations.append(Station(name, lat, lon, dep))
    refresh_listbox()


def on_sort():
    # TODO: stations 를 수심순으로 정렬 (sorted 또는 .sort()).
    #       Station.__lt__ 가 사용된다.
    stations.sort()
    refresh_listbox()


def on_delete():
    sel = listbox.curselection()
    if not sel:
        return
    del stations[sel[0]]
    refresh_listbox()


## 메인 코드 부분 ##
window = Tk()
window.title("연습 14 - 관측 정점 관리")
window.geometry("480x360")

# 입력 영역
top = Frame(window); top.pack(fill=X, pady=6)
for i, (lab, w) in enumerate([("이름", 6), ("위도", 7), ("경도", 7), ("수심", 6)]):
    Label(top, text=lab).grid(row=0, column=2*i, padx=2)
e_name = Entry(top, width=6);  e_name.grid(row=0, column=1)
e_lat  = Entry(top, width=7);  e_lat.grid(row=0, column=3)
e_lon  = Entry(top, width=7);  e_lon.grid(row=0, column=5)
e_dep  = Entry(top, width=6);  e_dep.grid(row=0, column=7)
e_name.insert(0, "ST-D"); e_lat.insert(0, "35.0"); e_lon.insert(0, "129.0"); e_dep.insert(0, "80")

btns = Frame(window); btns.pack(fill=X, pady=4)
Button(btns, text="추가",       width=10, command=on_add).pack(side=LEFT, padx=4)
Button(btns, text="수심순 정렬", width=12, command=on_sort).pack(side=LEFT, padx=4)
Button(btns, text="선택 삭제",   width=10, command=on_delete).pack(side=LEFT, padx=4)

listbox = Listbox(window, font=("Consolas", 11))
listbox.pack(fill=BOTH, expand=True, padx=10, pady=8)

refresh_listbox()
window.mainloop()
