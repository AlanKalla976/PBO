import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def hitung_luas():
    alas = float(txtalas.get())
    tinggi_limas = float(txttinggi_limas.get())
    tinggi_segitiga = float(txttinggi_segitiga.get())

    L = round (alas * tinggi_limas) / 2 + 3 * (0.5 * alas * tinggi_segitiga)

    txtluas.delete(0,END)
    txtluas.insert(END,L)

def hitung_volume():
    alas = float(txtalas.get())
    tinggi_limas = float(txttinggi_limas.get())
    tinggi_segitiga = float(txttinggi_segitiga.get())

    V = round  (alas ** 2 * tinggi_segitiga) / 6

    txtvolume.delete(0,END)
    txtvolume.insert(END,V)

def hitung():
    hitung_luas()
    hitung_volume()

# Membuat GUI
app = tk.Tk()
app.title("menghitung luas dan volume Limas Segitiga")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Nama
nama = Label(frame, text="Nama : Alan Kalla / 220511076")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label alas
alas_label = Label(frame, text="alas")
alas_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Label tinggi limas
tinggi_limas = Label(frame, text="Tinggi limas")
tinggi_limas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Label tinggi segitiga
tinggi_segitiga = Label(frame, text="Tinggi segitiga")
tinggi_segitiga.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Textbox alas
txtalas = Entry(frame)
txtalas.grid(row=2, column=1)

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