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
def adoctor():
    try:
        cur.execute('CREATE TABLE IF NOT EXISTS doctor(DID int,NAME varchar(20),DEPT varchar(20),FEES int,ROOM int,PRIMARY KEY (DID))')
        q='insert into doctor values(%s,%s,%s,%s,%s)'
        did=int(input('Enter Doctor ID: '))
        name=input('Enter Name of the Doctor: ')
        dept=input('Enter Department of the Doctor: ')
        fees=int(input('Enter Fees of the Doctor'))
        room=int(input('Enter Room No. of the Doctor: '))
        v=did,name,dept,fees,room
        cur.execute(q,v)
        con.commit()
    except mycc.Error as E:
        print(E.msg)
def rdoctor():
    try:
        id=int(input('Enter Doctor ID to Remove from Database'))
        v=(id,)
        q='delete from doctor where id=%s'
        cur.execute(q,v)
    except mycc.Error as E:
        print(E.msg)
def udoctor():
    try:
        t3=Texttable()
        t3.set_cols_align(['c'])
        t3.set_cols_valign(['m'])
        t3.add_rows([['LOGGED IN AS ADMIN'],
                     [''],
                     ['1. Update NAME'],
                     ['2. Update DEPARTMENT'],
                     ['3. Update FEES'],
                     ['4. Update ROOM No.']
                     ])
        t3.draw()
        c=int(input('Enter Choice: '))
        if c==1:
            id=int(input('Enter Doctor ID: '))
            name=input('Enter Update Doctor Name: ')
            v=name,id
            q='update doctor set name=%s where id=%s'
            cur.execute(q,v)
            con.commit()
            print('Name Updated')
        if c==2:
            id=int(input('Enter Doctor ID: '))
            dept=input('Enter Update Doctor Department: ')
            v=dept,id
            q='update doctor set dept=%s where id=%s'
            cur.execute(q,v)
            con.commit()
            print('Department Updated')
        if c==3:
            id=int(input('Enter Doctor ID: '))
            fees=input('Enter Update Doctor Fees: ')
            v=fees,id
            q='update doctor set fees=%s where id=%s'
            cur.execute(q,v)
            con.commit()
            print('Fees Updated')
        if c==4:
            id=int(input('Enter Doctor ID: '))
            room=input('Enter Update Doctor Room no.: ')
            v=dept,id
            q='update doctor set room=%s where id=%s'
            cur.execute(q,v)
            con.commit()
            print('Room No. Updated')
    except mycc.Error as E:
        print(E.msg)
def ddoctor():
    try:
        q='delete from doctor where id=%s'
        id=int(input('Enter Doctor ID: '))
        v=(id,)
        cur.execute(q,v)
        con.commit()
    except mycc.Error as E:
        print(E.msg)
def disdoctor():
    try:
        q='select * from doctor'
        cur.execute(q)
        t4=Texttable()
        t4.set_cols_align(['c','c','c','c','c',])
        t4.set_cols_valign(['m'])
        t4.add_rows([['DID','NAME','DEPT','FEES','ROOM No.']])
        r=cur.fetchall()
        for x in r:
            t4.addrow([x])
        t4.draw()
        
def upatient():
    cur.execute('CREATE TABLE IF NOT EXISTS patient(PID int,USERNAME varchar(15),NAME varchar(20),AGE int,BLOOD_GROUP varchar(3),DID int,PRIMARY KEY (PID),FOREIGN KEY (DID) references doctor(DID)),FOREIGN KEY (USERNAME) references login(USERNAME))')
    try:
        t5=Texttable()
        t5.set_cols_align(['c'])
        t5.set_cols_valign(['m'])
        t5.add_rows([['LOGGED IN AS ADMIN'],
                     [''],
                     ['1. Update PATIENT'],
                     ['2. Update DEPARTMENT'],
                     ['3. Update FEES'],
                     ['4. Update ROOM No.']
                     ])
        t5.draw()
        c=int(input('Enter Choice: '))
        if c==1:
            id=int(input('Enter Doctor ID: '))
            name=input('Enter Update Doctor Name: ')
            v=name,id
            q='update doctor set name=%s where id=%s'
            cur.execute(q,v)
            con.commit()
            print('Name Updated')
        if c==2:
            id=int(input('Enter Doctor ID: '))
            dept=input('Enter Update Doctor Department: ')
            v=dept,id
            q='update doctor set dept=%s where id=%s'
            cur.execute(q,v)
            con.commit()
            print('Department Updated')
        if c==3:
            id=int(input('Enter Doctor ID: '))
            fees=input('Enter Update Doctor Fees: ')
            v=fees,id
            q='update doctor set fees=%s where id=%s'
            cur.execute(q,v)
            con.commit()
            print('Fees Updated')
        if c==4:
            id=int(input('Enter Doctor ID: '))
            room=input('Enter Update Doctor Room no.: ')
            v=dept,id
            q='update doctor set room=%s where id=%s'
            cur.execute(q,v)
            con.commit()
            print('Room No. Updated')
    except mycc.Error as E:
        print(E.msg)    