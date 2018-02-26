#coding:utf-8
import pyodbc
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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

outputMode='{0:<20}{1:{4}<10}{2:<20}{3:<60}'
#既有英文又有中文输出还是不整齐
print outputMode.format(u'登录账号',u'名称',u'账号',u'密码',unichr(12288))
for i in result:
    print outputMode.format(i[2],i[3],i[4],i[5],unichr(12288))
