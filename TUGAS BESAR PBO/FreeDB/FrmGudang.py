import tkinter as tk
from tkinter import Frame, Label, Entry, Button, Radiobutton, ttk, END, StringVar, messagebox
from tkcalendar import DateEntry
from gudang_semuadata import gudang

class Formgudang:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.geometry("850x550")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=tk.BOTH, expand=tk.YES)
        mainFrame.configure(background='light blue')

        Label(mainFrame, text='Nama Barang:', bg='lightblue').grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtNama_Barang = Entry(mainFrame)
        self.txtNama_Barang.grid(row=0, column=1, padx=5, pady=5)
        self.txtNama_Barang.bind("<Return>", self.onCari)

        Label(mainFrame, text='Jumlah Barang:', bg='lightblue').grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtJumlah_Barang = Entry(mainFrame)
        self.txtJumlah_Barang.grid(row=1, column=1, padx=5, pady=5)

        Label(mainFrame, text='Tanggal:', bg='lightblue').grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtTanggal = DateEntry(mainFrame, date_pattern='yyyy-mm-dd')
        self.txtTanggal.grid(row=2, column=1, padx=5, pady=5)

        Label(mainFrame, text='Stock Gudang:', bg='lightblue').grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtStock_gudang = Entry(mainFrame)
        self.txtStock_gudang.grid(row=3, column=1, padx=5, pady=5)

        Label(mainFrame, text='Tipe Transaksi:', bg='lightblue').grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtTipe_Transaksi = StringVar()
        self.L = Radiobutton(mainFrame, text='Masuk', value='Masuk', variable=self.txtTipe_Transaksi, bg='lightblue')
        self.L.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)
        self.L.select()
        self.P = Radiobutton(mainFrame, text='Keluar', value='Keluar', variable=self.txtTipe_Transaksi, bg='lightblue')
        self.P.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)

        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10, bg='green')
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10, bg='lightgreen')
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10, bg='red')
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        self.btnEdit = Button(mainFrame, text='Edit', command=self.onEdit, width=10, bg='lightgreen')
        self.btnEdit.grid(row=3, column=3, padx=5, pady=5)

        columns = ('id', 'nama barang', 'jumlah barang', 'tipe transaksi', 'tanggal', 'stock gudang')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('nama barang', text='Nama Barang')
        self.tree.column('nama barang', width="150")
        self.tree.heading('jumlah barang', text='Jumlah Barang')
        self.tree.column('jumlah barang', width="150")
        self.tree.heading('tipe transaksi', text='Tipe Transaksi')
        self.tree.column('tipe transaksi', width="150")
        self.tree.heading('tanggal', text='Tanggal')
        self.tree.column('tanggal', width="150")
        self.tree.heading('stock gudang', text='Stock Gudang')
        self.tree.column('stock gudang', width="150")

        self.tree.place(x=0, y=250)
        self.onReload()

    def onClear(self, event=None):
        self.txtNama_Barang.delete(0, END)
        self.txtNama_Barang.insert(END, "")
        self.txtJumlah_Barang.delete(0, END)
        self.txtJumlah_Barang.insert(END, "")
        self.txtTanggal.set_date(None)
        self.txtStock_gudang.delete(0, END)
        self.txtStock_gudang.insert(END, "")
        self.btnSimpan.config(text="Simpan")
        self.L.select()
        self.onReload()
        self.ditemukan = False

    def onReload(self, event=None):
        gd = gudang()
        result = gd.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        students = []
        for row_data in result:
            students.append(row_data)

        for student in students:
            self.tree.insert('', END, values=student)

    def onCari(self, event=None):
        nama_barang = self.txtNama_Barang.get()
        gd = gudang()
        res = gd.getByNama_Barang(nama_barang)
        rec = gd.affected
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan")
            self.ditemukan = False
            self.txtJumlah_Barang.focus()
        return res

    def TampilkanData(self, event=None):
        nama_barang = self.txtNama_Barang.get()
        gd = gudang()
        res = gd.getByNama_Barang(nama_barang)
        self.txtJumlah_Barang.delete(0, END)
        self.txtJumlah_Barang.insert(END, res[2])
        tipe_transaksi = gd.tipe_transaksi
        if tipe_transaksi == "P":
            self.P.select()
        else:
            self.L.select()
        self.btnSimpan.config(text="Update")

    def onSimpan(self, event=None):
        nama_barang = self.txtNama_Barang.get()
        jumlah_barang = self.txtJumlah_Barang.get()
        tipe_transaksi = self.txtTipe_Transaksi.get()
        tanggal = self.txtTanggal.get()
        stock_gudang = self.txtStock_gudang.get()

        gd = gudang()
        gd.nama_barang = nama_barang
        gd.jumlah_barang = jumlah_barang
        gd.tipe_transaksi = tipe_transaksi
        gd.tanggal = tanggal
        gd.stock_gudang = stock_gudang
        if self.ditemukan == True:
            res = gd.updateByNama_Barang(nama_barang)
            ket = 'Diperbarui'
        else:
            res = gd.simpan()
            ket = 'Disimpan'

        rec = gd.affected
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        nama_barang = self.txtNama_Barang.get()
        gd = gudang()
        gd.nama_barang = nama_barang
        if self.ditemukan == True:
            res = gd.deleteByNama_Barang(nama_barang)
            rec = gd.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0

        if rec > 0:
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")

        self.onClear()

    def onEdit(self, event=None):
        nama_barang = self.txtNama_Barang.get()
        if not nama_barang:
            messagebox.showwarning("showwarning", "Pilih data yang ingin diedit.")
            return

        gd = gudang()
        res = gd.getByNama_Barang(nama_barang)
        rec = gd.affected
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan")
            self.ditemukan = False
            self.txtJumlah_Barang.focus()

    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = Formgudang(root, "Aplikasi Data Gudang")
    root.mainloop()