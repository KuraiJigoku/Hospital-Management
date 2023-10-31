import myc
import mysql.connector as mycc
from texttable import Texttable
u=input('Enter Admin Username: ')
p=input('Enter Admin Password: ')
con,cur=myc.connection()
try:
    cur.execute("insert ignore into login values('admin','radcliff','ADMIN')")
    con.commit()
except mycc.Error as E:
    print(E.msg)


def login():
    v=(u,)
    q='select * from login where username=%s'
    cur.execute(q,v)
    t=''
    for x in cur:
        if x[1]==p:
            t='True'
    return t
t=login()
if t=="True":
    print('harry')

