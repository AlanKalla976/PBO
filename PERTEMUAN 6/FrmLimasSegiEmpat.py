from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W
import math

class FrmLimasSegiEmpat:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Panjang Sisi Alas:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tinggi Segi Empat:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tinggi Limas:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Volume:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Luas:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)

        self.txtPanjangSisi = Entry(mainFrame)
        self.txtPanjangSisi.grid(row=0, column=1, padx=5, pady=5)
        self.txtTinggiSegiEmpat = Entry(mainFrame)
        self.txtTinggiSegiEmpat.grid(row=1, column=1, padx=5, pady=5)
        self.txtTinggiLimas = Entry(mainFrame)
        self.txtTinggiLimas.grid(row=2, column=1, padx=5, pady=5)
        self.txtVolume = Entry(mainFrame)
        self.txtVolume.grid(row=4, column=1, padx=5, pady=5)
        self.txtluas = Entry(mainFrame)
        self.txtluas.grid(row=5, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)

    def onHitung(self, event=None):
        try:
            #menghitung volume
            panjang_sisi_alas = float(self.txtPanjangSisi.get())
            tinggi_segi_empat = float(self.txtTinggiSegiEmpat.get())
            tinggi_limas = float(self.txtTinggiLimas.get())
            volume = (1/3) * (panjang_sisi_alas**2) * tinggi_segi_empat * tinggi_limas
            self.txtVolume.delete(0, END)
            self.txtVolume.insert(END, str(volume))
            #menghitung luas
            panjang_sisi_alas = float(self.txtPanjangSisi.get())
            tinggi_segi_empat = float(self.txtTinggiSegiEmpat.get())
            tinggi_limas = float(self.txtTinggiLimas.get())
            luas = (1/3) * (panjang_sisi_alas**2) * tinggi_segi_empat * tinggi_limas
            self.txtluas.delete(0, END)
            self.txtluas.insert(END, str(luas))
        except ValueError:
            self.txtVolume.delete(0, END)
            self.txtVolume.insert(END, "Invalid Input")

    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = FrmLimasSegiEmpat(root, "Program Volume Limas Segi Empat")
    root.mainloop()
