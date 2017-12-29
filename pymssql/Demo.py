#coding:utf-8

import pyodbc

class MSSQL:
    def __init__(self,host,user,pwd,db):
        self.host=host
        self.user=user
        self.pwd=pwd
        self.db=db

    def __GetConnect(self):
        if not self.db:
            raise NameError,'没有设置数据库信息'
        # self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=self.host;DATABASE=self.db;UID=self.user;PWD=self.pwd')
        self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.1.167,3341;DATABASE=DB_SLSAutoAccount;UID=sa;PWD=sls_taobao')
        cur=self.conn.cursor()
        if not cur:
            raise NameError,'连接数据库失败'
        else:
            return cur

    def ExecQuery(self,sql):
        cur=self.__GetConnect()
        cur.execute(sql)
        resList=cur.fetchall()

        #查询结束，关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        cur=self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

ms=MSSQL(host="192.168.1.167,3341",user="sa",pwd="sls_taobao",db="DB_SLSAutoAccount")

resList=ms.ExecQuery("select * from tb_YYSAccount")

for i in resList:
    print i