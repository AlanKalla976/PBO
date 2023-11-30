from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W, StringVar
import math

class FrmBola:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Jari-Jari:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Volume:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Luas:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)

        self.txtJariJari = Entry(mainFrame)
        self.txtJariJari.grid(row=0, column=1, padx=5, pady=5)
        self.txtVolume = Entry(mainFrame)
        self.txtVolume.grid(row=2, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=3, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=1, column=1, padx=5, pady=5)

    def onHitung(self, event=None):
        try:
            #menghitung volume
            jari_jari = float(self.txtJariJari.get())
            volume = round ((4/3) * math.pi * jari_jari**3)
            self.txtVolume.delete(0, END)
            self.txtVolume.insert(END, str(volume))
            #menghitung luas
            jari_jari = float(self.txtJariJari.get())
            luas = round (4 * math.pi * (jari_jari ** 2))
            self.txtLuas.delete(0, END)
            self.txtLuas.insert(END, str(luas))
        except ValueError:
            self.txtVolume.delete(0, END)
            self.txtVolume.insert(END, "Invalid Input")

    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = FrmBola(root, "Program Volume Bola")
    root.mainloop()
