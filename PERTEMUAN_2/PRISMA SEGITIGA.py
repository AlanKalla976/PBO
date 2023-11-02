import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def hitung_luas():
    alas_segitiga = float(txtalas_segitiga.get())
    tinggi_segitiga = float(txttinggi_segitiga.get())
    tinggi_prisma= float(txttinggi_prisma.get())

    L = round (alas_segitiga * tinggi_prisma) + 2 * (0.5 * alas_segitiga * tinggi_segitiga)

    txtluas.delete(0,END)
    txtluas.insert(END,L)

def hitung_volume():
    alas_segitiga = float(txtalas_segitiga.get())
    tinggi_segitiga = float(txttinggi_segitiga.get())
    tinggi_prisma = float(txttinggi_prisma.get())

    V = round  (0.5 * alas_segitiga * tinggi_segitiga * tinggi_prisma)

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

# Label alas segitiga
alas_segitiga_label = Label(frame, text="alas segitiga")
alas_segitiga_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Label tinggi segitiga
tinggi_segitiga = Label(frame, text="Tinggi segitiga")
tinggi_segitiga.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Label tinggi prisma
tinggi_prisma = Label(frame, text="Tinggi prisma")
tinggi_prisma.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Textbox alas segitiga
txtalas_segitiga = Entry(frame)
txtalas_segitiga.grid(row=2, column=1)

# Textbox tinggi segitiga
txttinggi_segitiga = Entry(frame)
txttinggi_segitiga.grid(row=3, column=1)

# Textbox tinggi prisma
txttinggi_prisma = Entry(frame)
txttinggi_prisma.grid(row=4, column=1)

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