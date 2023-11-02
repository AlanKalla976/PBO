import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def hitung_luas():
    sisi_alas = float(txtsisi_alas.get())
    tinggi_limas = float(txttinggi_limas.get())
    tinggi_segitiga = float(txttinggi_segitiga.get())

    L = round (sisi_alas ** 2) + 2 * sisi_alas * (tinggi_limas + tinggi_segitiga)

    txtluas.delete(0,END)
    txtluas.insert(END,L)

def hitung_volume():
    sisi_alas = float(txtsisi_alas.get())
    tinggi_limas = float(txttinggi_limas.get())
    tinggi_segitiga = float(txttinggi_segitiga.get())

    V = round (sisi_alas ** 2 * tinggi_limas) / 3

    txtvolume.delete(0,END)
    txtvolume.insert(END,V)

def hitung():
    hitung_luas()
    hitung_volume()

# Membuat GUI
app = tk.Tk()
app.title("menghitung luas dan volume Limas Segiempat")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Nama
nama = Label(frame, text="Nama : Alan Kalla / 220511076")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label sisi alas
sisi_alas_label = Label(frame, text="Sisi alas")
sisi_alas_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Label tinggi limas
tinggi_limas = Label(frame, text="Tinggi limas")
tinggi_limas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Label tinggi segitiga
tinggi_segitiga = Label(frame, text="Tinggi segitiga")
tinggi_segitiga.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Textbox sisi alas
txtsisi_alas = Entry(frame)
txtsisi_alas.grid(row=2, column=1)

# Textbox tinggi limas
txttinggi_limas = Entry(frame)
txttinggi_limas.grid(row=3, column=1)

# Textbox tinggi segitiga
txttinggi_segitiga = Entry(frame)
txttinggi_segitiga.grid(row=4, column=1)

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