import tkinter as tk
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Tạo khóa nhanh
pri = rsa.generate_private_key(65537, 2048)
pub = pri.public_key()

def run(mode):
    try:
        if mode == 'en':
            c = pub.encrypt(ent.get().encode(), padding.PKCS1v15())
            res.delete("1.0", tk.END); res.insert(tk.END, c.hex())
        else:
            p = pri.decrypt(bytes.fromhex(res.get("1.0", tk.END).strip()), padding.PKCS1v15())
            ent.delete(0, tk.END); ent.insert(0, p.decode())
    except: tk.messagebox.showerror("Error", "Loi du lieu!")

root = tk.Tk()
root.title("RSA - Dat 0423")

ent = tk.Entry(root, width=40); ent.pack(pady=5)
tk.Button(root, text="MA HOA", command=lambda: run('en')).pack()
tk.Button(root, text="GIAI MA", command=lambda: run('de')).pack()
res = tk.Text(root, width=40, height=5); res.pack(pady=5)

root.mainloop()