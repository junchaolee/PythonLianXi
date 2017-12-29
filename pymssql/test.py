#coding:utf-8
import pyodbc
conn = pyodbc.connect(
    r'DRIVER={SQL Server};'
    r'SERVER=192.168.1.167,3341;'
    r'DATABASE=DB_SLSAutoAccount;'
    r'UID=sa;'
    r'PWD=sls_taobao'
    )
mycursor=conn.cursor()
mycursor.execute("select top 10 * from tb_YYSAccount")
result=mycursor.fetchall()
print 'loginaccount\tyys\t\taacount\t\tpwd\t\t'
for i in result:
    print i[2]+"\t\t"+i[3]+"\t\t"+i[4]+"\t\t"+i[5]