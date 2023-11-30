import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def hitung_luas():
    pj = float(txtpanjang.get())
    lb = float(txtlebar.get())
    t = float(txttinggi.get())

    L = round (2 * ((pj * lb) + (pj * t) + (lb * t)),2)

    txtluas.delete(0,END)
    txtluas.insert(END,L)

def hitung_volume():
    pj = float(txtpanjang.get())
    lb = float(txtlebar.get())
    t = float(txttinggi.get())

    V = round (pj * lb * t)

    txtvolume.delete(0,END)
    txtvolume.insert(END,V)

def hitung():
    hitung_luas()
    hitung_volume()

# Membuat GUI
app = tk.Tk()
app.title("menghitung luas dan volume balok")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Nama
nama = Label(frame, text="Nama : Alan Kalla / 220511076")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label panjang
panjang_label = Label(frame, text="Panjang")
panjang_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Label lebar
lebar = Label(frame, text="Lebar")
lebar.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Label tinggi
tinggi = Label(frame, text="Tinggi")
tinggi.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Textbox panjang
txtpanjang = Entry(frame)
txtpanjang.grid(row=2, column=1)

# Textbox lebar
txtlebar = Entry(frame)
txtlebar.grid(row=3, column=1)

# Textbox tinggi
txttinggi= Entry(frame)
txttinggi.grid(row=4, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas_label = Label(frame, text="Luas")
luas_label.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtluas = Entry(frame)
txtluas.grid(row=6, column=1)

# Output Label Volume
volume_label = Label(frame, text="Volume")
volume_label.grid(row=7, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtvolume = Entry(frame)
txtvolume.grid(row=7, column=1)

app.mainloop()