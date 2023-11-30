from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W
import math

class FrmLimasSegitiga:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Panjang Alas Segitiga:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tinggi Segitiga:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tinggi Limas:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Volume:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Luas:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)

        self.txtPanjangAlas = Entry(mainFrame)
        self.txtPanjangAlas.grid(row=0, column=1, padx=5, pady=5)
        self.txtTinggiSegitiga = Entry(mainFrame)
        self.txtTinggiSegitiga.grid(row=1, column=1, padx=5, pady=5)
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
            panjang_alas_segitiga = float(self.txtPanjangAlas.get())
            tinggi_segitiga = float(self.txtTinggiSegitiga.get())
            tinggi_limas = float(self.txtTinggiLimas.get())
            volume = (1/3) * (panjang_alas_segitiga * tinggi_segitiga) * tinggi_limas
            self.txtVolume.delete(0, END)
            self.txtVolume.insert(END, str(volume))
            #menghitung luas
            panjang_alas_segitiga = float(self.txtPanjangAlas.get())
            tinggi_segitiga = float(self.txtTinggiSegitiga.get())
            tinggi_limas = float(self.txtTinggiLimas.get())
            luas =  round (panjang_alas_segitiga * tinggi_limas) / 2 + 3 * (0.5 * panjang_alas_segitiga * tinggi_segitiga)
            self.txtluas.delete(0, END)
            self.txtluas.insert(END, str(luas))
        except ValueError:
            self.txtVolume.delete(0, END)
            self.txtVolume.insert(END, "Invalid Input")

    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = FrmLimasSegitiga(root, "Program Volume Limas Segitiga")
    root.mainloop()
