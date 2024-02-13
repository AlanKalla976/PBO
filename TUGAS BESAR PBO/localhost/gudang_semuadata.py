from db import DBConnection as mydb

class gudang:
    def __init__(self):
        self.__id = None
        self.__nama_barang = None
        self.__jumlah_barang = None
        self.__tanggal = None
        self.__tipe_transaksi = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def id(self):
        return self.__id

    @property
    def nama_barang(self):
        return self.__nama_barang

    @nama_barang.setter
    def nama_barang(self, value):
        self.__nama_barang = value

    @property
    def jumlah_barang(self):
        return self.__jumlah_barang

    @jumlah_barang.setter
    def jumlah_barang(self, value):
        self.__jumlah_barang = value

    @property
    def tipe_transaksi(self):
        return self.__tipe_transaksi

    @tipe_transaksi.setter
    def tipe_transaksi(self, value):
        self.__tipe_transaksi = value

    @property
    def stock_gudang(self):
        return self.__stock_gudang

    @stock_gudang.setter
    def stock_gudang(self, value):
        self.__stock_gudang = value

    @property
    def tanggal(self):
        return self.__tanggal

    @tanggal.setter
    def tanggal(self, value):
        self.__tanggal = value


        
    def simpan(self):

        self.conn = mydb()
        val = (self.__nama_barang, self.__jumlah_barang, self.__tanggal, self.__stock_gudang, self.__tipe_transaksi)
        sql = "INSERT INTO gudang (nama_barang, jumlah_barang, tanggal, stock_gudang, tipe_transaksi) VALUES (%s, %s, %s, %s, %s)"
        self.affected = self.conn.insert(sql, val)
        self.conn.disconnect()
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__nama_barang, self.__jumlah_barang, self.__tanggal, self.__stock_gudang, self.__tipe_transaksi, id)
        sql = "UPDATE gudang SET nama_barang = %s, jumlah_barang = %s, tanggal = %s, stock_gudang = %s, tipe_transaksi=%s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect()
        return self.affected

    def updateByNama_Barang(self, nama_barang):
        self.conn = mydb()
        val = (self.__jumlah_barang, self.__tanggal, self.__stock_gudang, self.__tipe_transaksi, nama_barang)
        sql = "UPDATE gudang SET jumlah_barang = %s, tanggal = %s, stock_gudang = %s, tipe_transaksi=%s WHERE nama_barang=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect()
        return self.affected    

    def delete(self, id):
        self.conn = mydb()
        sql = "DELETE FROM gudang WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect()
        return self.affected

    def deleteByNama_Barang(self, nama_barang):
        self.conn = mydb()
        sql = "DELETE FROM gudang WHERE nama_barang='" + str(nama_barang) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect()
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql = "SELECT * FROM gudang WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__nama_barang = self.result[1]
        self.__jumlah_barang = self.result[2]
        self.__tanggal = self.result[3]
        self.__stock_gudang = self.result[4]
        self.__tipe_transaksi = self.result[5]
        self.conn.disconnect()
        return self.result

    def getByNama_Barang(self, nama_barang):
        a = str(nama_barang)
        b = a.strip()
        self.conn = mydb()
        sql = "SELECT * FROM gudang WHERE nama_barang='" + b + "'"
        self.result = self.conn.findOne(sql)
        if self.result != None:
            self.__nama_barang = self.result[1]
            self.__jumlah_barang = self.result[2]
            self.__tanggal = self.result[3]
            self.__stock_gudang = self.result[4]
            self.__tipe_transaksi = self.result[5]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nama_barang = ''
            self.__jumlah_barang = ''
            self.__tanggal = ''
            self.__stock_gudang = ''
            self.__tipe_transaksi = ''
            self.affected = 0
        self.conn.disconnect()
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql = "SELECT * FROM gudang"
        self.result = self.conn.findAll(sql)
        return self.result