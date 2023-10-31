import myc
import mysql.connector as mycc
from texttable import Texttable
con,cur=myc.connection()
try:
    cur.execute('CREATE TABLE IF NOT EXISTS login(USERNAME varchar(15),PASSWORD varchar(20),ROLE varchar(10),PRIMARY KEY (USERNAME))')
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
    global t
    t=''
    for x in cur:
        if x[1]==p:
            t='True'
def addd():
    cur.execute('CREATE TABLE IF NOT EXISTS doctor(DID int,NAME varchar(20),DEPT varchar(20),FEES int,ROOM int,PRIMARY KEY (DID))')
    q='insert into doctor values()'
