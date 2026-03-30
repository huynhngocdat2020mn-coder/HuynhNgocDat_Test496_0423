import tkinter as tk

def rail_fence(text, key, encrypt=True):
    if key < 2: return text
    rail = [['' for _ in range(len(text))] for _ in range(key)]
    row, step = 0, 1
    
    # Tạo khung zic-zac
    idx_map = []
    for i in range(len(text)):
        idx_map.append(row)
        if row == 0: step = 1
        elif row == key - 1: step = -1
        row += step

    if encrypt:
        # Gom ký tự theo hàng
        return "".join("".join(text[i] for i, r in enumerate(idx_map) if r == j) for j in range(key))
    else:
        # Giải mã (điền ngược lại)
        result, pos = [''] * len(text), 0
        for r in range(key):
            for i, row_idx in enumerate(idx_map):
                if row_idx == r:
                    result[i] = text[pos]
                    pos += 1
        return "".join(result)

# UI cực gọn
def run(mode):
    try:
        res = rail_fence(ent_t.get(), int(ent_k.get()), mode=="en")
        lbl_r.config(text=res)
    except: lbl_r.config(text="Lỗi Key!")

root = tk.Tk()
root.title("Rail Fence - Dat 0423")

tk.Label(root, text="Text:").pack()
ent_t = tk.Entry(root); ent_t.pack()
tk.Label(root, text="Key:").pack()
ent_k = tk.Entry(root, width=5); ent_k.pack()

tk.Button(root, text="Mã hóa", command=lambda: run("en")).pack()
tk.Button(root, text="Giải mã", command=lambda: run("de")).pack()
lbl_r = tk.Label(root, text="KQ", fg="red", font=("Arial", 12, "bold"))
lbl_r.pack()

root.mainloop()