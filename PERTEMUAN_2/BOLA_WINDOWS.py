import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W
from math import pi

def hitung_luas():
    j = float(txtjari_jari.get())

    L = round (4 * pi * (j ** 2))

    txtluas.delete(0,END)
    txtluas.insert(END,L)

def hitung_volume():
    j = float(txtjari_jari.get())

    V = round ((4/3) * pi * (j ** 3))

    txtvolume.delete(0,END)
    txtvolume.insert(END,V)

def hitung():
    hitung_luas()
    hitung_volume()

# Membuat GUI
app = tk.Tk()
app.title("menghitung luas dan volume bola")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Nama
nama = Label(frame, text="Nama : Alan Kalla / 220511076")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label jari-jari
jari_jari_label = Label(frame, text="jari-jari")
jari_jari_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Textbox  jari-jari
txtjari_jari = Entry(frame)
txtjari_jari.grid(row=2, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas_label = Label(frame, text="Luas")
luas_label.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtluas = Entry(frame)
txtluas.grid(row=4, column=1)

# Output Label Volume
volume_label = Label(frame, text="Volume")
volume_label.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtvolume = Entry(frame)
txtvolume.grid(row=5, column=1)

app.mainloop()