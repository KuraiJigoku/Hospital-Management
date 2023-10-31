import myc
import mysql.connector as mycc
from texttable import Texttable
con,cur=myc.connection()
try:
    cur.execute("insert ignore into login values('admin','radcliff','ADMIN')")
    con.commit()
except mycc.Error as E:
    print(E.msg)

u=input('Enter Admin Username: ')
p=input('Enter Admin Password: ')

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
    try:
        print('1. Hospital Managing')

