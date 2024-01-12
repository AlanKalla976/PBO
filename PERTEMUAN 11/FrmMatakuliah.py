import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from matakuliah_semuadata import matakuliah

class Formmatakuliah:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        # set warna latar belakang
        mainFrame.configure(background='light green')
        
        # Label
        Label(mainFrame, text='KODEMK:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtKODEMK = Entry(mainFrame) 
        self.txtKODEMK.grid(row=0, column=1, padx=5, pady=5) 
        self.txtKODEMK.bind("<Return>",self.onCari) # menambahkan event Enter key

        Label(mainFrame, text='Namamk:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtNamamk = Entry(mainFrame) 
        self.txtNamamk.grid(row=1, column=1, padx=5, pady=5) 

        Label(mainFrame, text='sks:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtSKS = StringVar()
        self.L = Radiobutton(mainFrame, text='1', value='1', variable=self.txtSKS)
        self.L.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        self.L.select() # set pilihan yg pertama
        self.P = Radiobutton(mainFrame, text='2', value='2', variable=self.txtSKS)
        self.P.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        self.P = Radiobutton(mainFrame, text='3', value='3', variable=self.txtSKS)
        self.P.grid(row=4, column=1, padx=5, pady=5, sticky=W)
        self.P = Radiobutton(mainFrame, text='4', value='4', variable=self.txtSKS)
        self.P.grid(row=5, column=1, padx=5, pady=5, sticky=W)

        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # define columns
        columns = ('idmk', 'kodemk', 'namamk','sks')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('idmk', text='ID')
        self.tree.column('idmk', width="30")
        self.tree.heading('kodemk', text='KODEMK')
        self.tree.column('kodemk', width="60")
        self.tree.heading('namamk', text='Namamk')
        self.tree.column('namamk', width="200")
        self.tree.heading('sks', text='SKS')
        self.tree.column('sks', width="30")
    
        # set tree position
        self.tree.place(x=0, y=200)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtKODEMK.delete(0,END)
        self.txtKODEMK.insert(END,"")
        self.txtNamamk.delete(0,END)
        self.txtNamamk.insert(END,"")       
        # self.txtKodeProdi.set("")
        self.btnSimpan.config(text="Simpan")
        self.L.select()
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data matakuliah
        mk = matakuliah()
        result = mk.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        students=[]
        for row_data in result:
            students.append(row_data)

        for student in students:
            self.tree.insert('',END, values=student)
    
    def onCari(self, event=None):
        kodemk = self.txtKODEMK.get()
        mk = matakuliah()
        res = mk.getByKODEMK(kodemk)
        rec = mk.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtNamamk.focus()
        return res
        
    def TampilkanData(self, event=None):
        kodemk = self.txtKODEMK.get()
        mk = matakuliah()
        res = mk.getByKODEMK(kodemk)
        self.txtNamamk.delete(0,END)
        self.txtNamamk.insert(END,mk.namamk)
        sks = mk.sks
        if(sks=="P"):
            self.P.select()
        else:
            self.L.select()
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        kodemk = self.txtKODEMK.get()
        namamk = self.txtNamamk.get()
        sks = self.txtSKS.get()

        
        mk = matakuliah()
        mk.kodemk = kodemk
        mk.namamk = namamk
        mk.sks = sks
        if(self.ditemukan==True):
            res = mk.updateByKODEMK(kodemk)
            ket = 'Diperbarui'
        else:
            res = mk.simpan()
            ket = 'Disimpan'
            
        rec = mk.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        kodemk = self.txtKODEMK.get()
        mk = matakuliah()
        mk.kodemk = kodemk
        if(self.ditemukan==True):
            res = mk.deleteByKODEMK(kodemk)
            rec = mk.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = Formmatakuliah(root, "Aplikasi Data Matakuliah")
    root.mainloop() 