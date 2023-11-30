from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W
import math

class FrmKerucut:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Jari-Jari Alas:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tinggi Kerucut:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Garis Pelukis:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Volume:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='luas:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)

        self.txtJariJari = Entry(mainFrame)
        self.txtJariJari.grid(row=0, column=1, padx=5, pady=5)
        self.txtTinggiKerucut = Entry(mainFrame)
        self.txtTinggiKerucut.grid(row=1, column=1, padx=5, pady=5)
        self.txtGaris_Pelukis = Entry(mainFrame)
        self.txtGaris_Pelukis.grid(row=2, column=1, padx=5, pady=5)
        self.txtVolume = Entry(mainFrame)
        self.txtVolume.grid(row=4, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=5, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)

    def onHitung(self, event=None):
        try:
            #menghitung volume
            jari_jari_alas = float(self.txtJariJari.get())
            tinggi_kerucut = float(self.txtTinggiKerucut.get())
            garis_pelukis = float(self.txtGaris_Pelukis.get())
            volume = round ((1/3) * math.pi * jari_jari_alas**2 * tinggi_kerucut)
            self.txtVolume.delete(0, END)
            self.txtVolume.insert(END, str(volume))
            #menghitung luas
            jari_jari_alas = float(self.txtJariJari.get())
            tinggi_kerucut = float(self.txtTinggiKerucut.get())
            garis_pelukis = float(self.txtGaris_Pelukis.get())
            luas = round (math.pi * jari_jari_alas * (jari_jari_alas + garis_pelukis))
            self.txtLuas.delete(0, END)
            self.txtLuas.insert(END, str(luas))
        except ValueError:
            self.txtVolume.delete(0, END)
            self.txtVolume.insert(END, "Invalid Input")

    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = FrmKerucut(root, "Program Volume Kerucut")
    root.mainloop()
