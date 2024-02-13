import mysql.connector as mc

class DBConnection:

    def __init__(self):

        self.host = 'mysql-1d65cd5a-alankalla19-4e32.a.aivencloud.com'
        self.port = 19223
        self.name = 'defaultdb'
        self.user = 'avnadmin'
        self.password = 'AVNS_MBY2zZL33c2u3VWWnaS'
        self.conn = None
        self.cursor = None
        self.result = None
        self.connected = False
        self.affected = 0
        self.connect()
        
    @property
    def connection_status(self):
        return self.connected
    
    def connect(self):
        try:
            self.conn = mc.connect(host = self.host,
                                    port = self.port,
                                    database = self.name,
                                    user = self.user,
                                    password = self.password)

            self.connected = True
            self.cursor=self.conn.cursor()
        except mc.Error as e:
            self.connected = False
        return self.conn

    def disconnect(self):
        if(self.connected==True):
            self.conn.close
        else:
            self.conn = None

    def findOne(self, sql):
        self.connect()
        self.cursor.execute(sql)
        self.result = self.cursor.fetchone()
        return self.result

    def findAll(self, sql):
        self.connect()
        self.result = self.cursor.execute(sql)
        self.result = self.cursor.fetchall()
        return self.result

    def insert(self, sql):
        self.connect()  
        self.cursor.execute(sql)
        self.conn.commit()
        self.affected = self.cursor.rowcount        
        return self.affected

    def update(self, sql, val):
        self.connect()  
        self.cursor.execute(sql, val)
        self.conn.commit()
        self.affected = self.cursor.rowcount        
        return self.affected

    def delete(self, sql):
        self.connect()  
        self.cursor.execute(sql)
        self.conn.commit()
        self.affected = self.cursor.rowcount        
        return self.affected

    def show(self, sql):
        self.connect()
        self.cursor.execute(sql)
        self.result = self.cursor.fetchone()
        return self.result

    @property
    def info(self):
        if(self.connected==True):
            return "Server is running on " + self.host + ' using port ' + str(self.port)
        else:
            return "Server is offline."

# Test koneksi database
A = DBConnection()
B = A.info
print(B)

