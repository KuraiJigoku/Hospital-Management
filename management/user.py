"""
This module provides functions for managing patient accounts in a hospital management system.
It requires the mysqlc module to connect to a MySQL database and the texttable module to display formatted tables.
The functions in this module allow patients to log in and view their personal information and doctor details.
"""
import mysqlc
import mysql.connector as myc
from texttable import Texttable
con,cur=mysqlc.connection()
def login():
    global u
    global p
    u=input('Enter Patient Username: ')
    p=input('Enter Patient Password: ')
    v=(u,)
    q='select * from login where username=%s'
    cur.execute(q,v)
    global t
    t=''
    for x in cur:
        if x[1]==p:
            t='True'
    return t
k=False
def uuser():
    try:
        p1=Texttable()
        p1.set_cols_align(['l'])
        p1.set_cols_valign(['m'])
        p1.add_rows([['LOGGED IN AS PATIENT'],
                    ['1. Update My Username'],
                    ['2. Update My Password'],
                    ['3. Back']
                    ])
        while True:
            global k
            print(p1.draw())
            c=int(input('Enter Choice: '))
            if c==1:
                q='update login set username=%s where username=%s'
                q1='update patient set pid=%s where pid=%s'
                u1=input('Enter New Username: ')
                v=(u1,u)
                cur.execute(q,v)
                cur.execute(q1,v)
                con.commit()
                print('Username Updated')
                k=True
                break
            elif c==2:
                q='update login set password=%s where username=%s'
                p1=input('Enter New Password: ')
                v=(p1,u)
                cur.execute(q,v)
                con.commit()
                print('Password Updated')
                k=True
                break
            elif c==3:
                break
    except myc.Error as E:
        print(E.msg)

def dpatient():
        try:
            global k
            p1=Texttable()
            p1.set_cols_align(['l'])
            p1.set_cols_valign(['m'])
            p1.add_rows([['LOGGED IN AS PATIENT'],
                        ['1. Display My Details'],
                        ['2. Display My Doctor Details'],
                        ['3. Change User Details'],
                        ['4. Back']
                        ])
            while True:
                print(p1.draw())
                c=int(input('Enter Choice: '))
                if c==1:
                    q='select pid,name,gender,age,blood_group,remark from patient where pid=%s'
                    global pid
                    pid=u
                    v=(pid,)
                    cur.execute(q,v)
                    pp1=Texttable()
                    pp1.set_cols_align(["c","c","c","c","c","c"])
                    pp1.set_cols_valign(["m","m","m","m","m","m"])
                    pp1.set_cols_dtype(["t","t","t","i","t","t"])
                    pp1.add_row(["ID","NAME","GENDER","AGE","BLOOD GROUP","REMARKS"])
                    r=cur.fetchall()
                    for x in r:
                        pp1.add_row(x)
                    print(pp1.draw())
                    input('Press Enter to Continue')

                elif c==2:
                    q='select patient.name,doctor.name,dept,fees,room from patient,doctor where patient.did=doctor.did and pid=%s'
                    v=(pid,)
                    cur.execute(q,v)
                    pd1=Texttable()
                    pd1.set_cols_align(["c","c","c","c","c"])
                    pd1.set_cols_valign(["m","m","m","m","m"])
                    pd1.set_cols_dtype(["i","t","t","i","i"])
                    pd1.add_row(["PATIENT NAME","DOCTOR NAME","DEPT","FEES","ROOM No."])
                    r=cur.fetchall()
                    for x in r:
                        pd1.add_row(x)
                    print(pd1.draw())
                    input('Press Enter to Continue')

                elif c==3:
                    uuser()
                    if k:
                        break
                elif c==4:
                    break
        except myc.Error as E:
            print(E.msg)
