"""
This module contains functions for managing a bank's database. It includes functions for logging in as an admin, adding, removing, updating, and displaying doctors and patients in the database. 

Functions:
- login(): Logs in as an admin.
- adoctor(): Adds a doctor to the database.
- rdoctor(): Removes a doctor from the database.
- udoctor(): Updates a doctor's information in the database.
- ddoctor(): Displays all doctors in the database.
- apatient(): Adds a patient to the database.
- upatient(): Updates a patient's information in the database.
"""
import mysqlc
import management.bill as bill
import mysql.connector as myc
from texttable import Texttable
con,cur=mysqlc.connection()

try:
    cur.execute('CREATE TABLE IF NOT EXISTS login(USERNAME varchar(15),PASSWORD varchar(20),ROLE varchar(10),PRIMARY KEY (USERNAME))')
    cur.execute("insert ignore into login values('admin','radcliff','ADMIN')")
    con.commit()
except myc.Error as E:
    print(E.msg)



def login():
    u=input('Enter Admin Username: ')
    p=input('Enter Admin Password: ')
    v=(u,)
    q='select * from login where username=%s'
    cur.execute(q,v)
    global t
    t=''
    for x in cur:
        if x[1]==p:
            t='True'
    return t
def adoctor():
    try:
        cur.execute('CREATE TABLE IF NOT EXISTS doctor(DID int,NAME varchar(40),DEPT varchar(40),FEES int,ROOM int,PRIMARY KEY (DID))')
        q='insert into doctor values(%s,%s,%s,%s,%s)'
        did=int(input('Enter Doctor ID: '))
        name=input('Enter Name of the Doctor: ')
        dept=input('Enter Department of the Doctor: ')
        fees=int(input('Enter Fees of the Doctor: '))
        room=int(input('Enter Room No. of the Doctor: '))
        v=did,name,dept,fees,room
        cur.execute(q,v)
        con.commit()
    except myc.Error as E:
        print(E.msg)
def rdoctor():
    try:
        did=int(input('Enter Doctor ID to Remove from Database: '))
        q='delete from doctor where did=%s'
        v=(did,)
        cur.execute(q,v)
    except myc.Error as E:
        print(E.msg)
def udoctor():
    try:
        t6=Texttable()
        t6.set_cols_align(['l'])
        t6.set_cols_valign(['m'])
        t6.add_rows([['LOGGED IN AS ADMIN'],
                     ['1. Update NAME'],
                     ['2. Update DEPARTMENT'],
                     ['3. Update FEES'],
                     ['4. Update ROOM No.']
                     ])
        print(t6.draw())
        c=int(input('Enter Choice: '))
        if c==1:
            id=int(input('Enter Doctor ID: '))
            name=input('Enter Update Doctor Name: ')
            v=name,id
            q='update doctor set name=%s where did=%s'
            cur.execute(q,v)
            con.commit()
            print('Name Updated')
        if c==2:
            id=int(input('Enter Doctor ID: '))
            dept=input('Enter Update Doctor Department: ')
            v=dept,id
            q='update doctor set dept=%s where did=%s'
            cur.execute(q,v)
            con.commit()
            print('Department Updated')
        if c==3:
            id=int(input('Enter Doctor ID: '))
            fees=input('Enter Update Doctor Fees: ')
            v=fees,id
            q='update doctor set fees=%s where did=%s'
            cur.execute(q,v)
            con.commit()
            print('Fees Updated')
        if c==4:
            id=int(input('Enter Doctor ID: '))
            room=input('Enter Update Doctor Room no.: ')
            v=room,id
            q='update doctor set room=%s where did=%s'
            cur.execute(q,v)
            con.commit()
            print('Room No. Updated')
    except myc.Error as E:
        print(E.msg)
def ddoctor():
    try:
        q="select * from doctor"
        cur.execute(q)
        t7=Texttable()
        t7.set_cols_align(["c","c","c","c","c"])
        t7.set_cols_valign(["m","m","m","m","m"])
        t7.set_cols_dtype(["i","t","t","i","i"])
        t7.add_row(["DID","NAME","DEPT","FEES","ROOM No."])
        r=cur.fetchall()
        for x in r:
            t7.add_row(x)
        print(t7.draw())
    except myc.Error as E:
        print(E.msg)
def apatient():
    try:
        cur.execute('CREATE TABLE IF NOT EXISTS patient(PID varchar(15),NAME varchar(40),GENDER varchar(10),AGE int,BLOOD_GROUP varchar(3),REMARK varchar(70),DID int,PRIMARY KEY (PID),FOREIGN KEY (DID) references doctor(DID))')
        pid=input('Enter Patient Username: ')
        name=input('Enter Name of the Patient: ')
        age=int(input('Enter Age of the Patient: '))
        gender=input('Enter Gender of the Patient: ')
        blood_group=input('Enter Blood Group of the Patient: ')
        remark=input('Enter Remark of the Patient: ')
        did=int(input('Enter Doctor ID: '))
        q='insert into login values(%s,%s,%s)'
        v=pid,pid,'PATIENT'
        cur.execute(q,v)
        q='insert into patient values(%s,%s,%s,%s,%s,%s,%s)'
        v=pid,name,gender,age,blood_group,remark,did
        cur.execute(q,v)
        con.commit()
        bill.abill(pid,did)
    except myc.Error as E:
        print(E.msg)

def upatient():
    try:
        t8=Texttable()
        t8.set_cols_align(['l'])
        t8.set_cols_valign(['m'])
        t8.add_rows([['LOGGED IN AS ADMIN'],
                     ['1. Update NAME'],
                     ['2. Display AGE'],
                     ['3. Update BLOOD GROUP'],
                     ['4. Back']
                     ])
        while True:
            print(t8.draw())
            c=int(input('Enter Choice: '))
            if c==1:
                id=input('Enter Patient ID: ')
                name=input('Enter Update Patient Name: ')
                v=name,id
                q='update patient set name=%s where pid=%s'
                cur.execute(q,v)
                con.commit()
                print('Name Updated')
            elif c==2:
                id=input('Enter Patient ID: ')
                dept=input('Enter Update Patient Age: ')
                v=dept,id
                q='update patient set age=%s where pid=%s'
                cur.execute(q,v)
                con.commit()
                print('Age Updated')
            elif c==3:
                id=input('Enter Patient ID: ')
                fees=input('Enter Update Patient Blood Group: ')
                v=fees,id
                q='update doctor set blood_group=%s where pid=%s'
                cur.execute(q,v)
                con.commit()
                print('Blood Group Updated')
            elif c==4:
                break
    except myc.Error as E:
        print(E.msg)
def rpatient():
    try:
        q='delete from patient where pid=%s'
        id=input('Enter Patient ID: ')
        v=(id,)
        cur.execute(q,v)
        con.commit()
    except myc.Error as E:
        print(E.msg)
def dpatient():
    try:
        q="select * from patient"
        cur.execute(q)
        t9=Texttable()
        t9.set_cols_align(["c","c","c","c","c","c","c"])
        t9.set_cols_valign(["m","m","m","m","m","m","m"])
        t9.set_cols_dtype(["i","t","t","i","t","t","i"])
        t9.add_row(["PID","NAME","GENDER","AGE","BlOOD GROUP","REMARK","DID"])
        r=cur.fetchall()
        for x in r:
            t9.add_row(x)
        print(t9.draw())
    except myc.Error as E:
        print(E.msg)
