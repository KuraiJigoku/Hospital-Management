import mysqlc
import mysql.connector as myc
from texttable import Texttable
con,cur=mysqlc.connection()
def login():
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
def dpatient():
        try:
            p1=Texttable()
            p1.set_cols_align(['l'])
            p1.set_cols_valign(['m'])
            p1.add_rows([['LOGGED IN AS PATIENT'],
                        ['1. Display My Details'],
                        ['2. Display My Doctor Details'],
                        ['3. Back']
                        ])
            while True:
                print(p1.draw())
                c=int(input('Enter Choice: '))
                if c==1:
                    p2=Texttable()
                    p2.set_cols_align(['l'])
                    p2.set_cols_valign(['m'])
                    p2.add_rows([['DISPLAYING PATIENT DETAILS'],
                                 ['1. Search Using Patient ID'],
                                 ['2. Search Using Patient Name'],
                                 ['3. Back']
                                 ])
                    while True:
                        print(p2.draw())
                        c1=int(input('Enter Choice: '))
                        if c1==1:
                            q='select pid,name,gender,age,blood_group,remark from patient where pid=%s'
                            pid=input('Enter Patient ID: ')
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

                        elif c1==2:
                            q='select pid,name,gender,age,blood_group,remark from patient where name=%s'
                            name=input('Enter Patient Name: ')
                            v=(name,)
                            cur.execute(q,v)
                            pp2=Texttable()
                            pp2.set_cols_align(["c","c","c","c","c","c"])
                            pp2.set_cols_valign(["m","m","m","m","m","m"])
                            pp2.set_cols_dtype(["t","t","t","i","t","t"])
                            pp2.add_row(["ID","NAME","GENDER","AGE","BLOOD GROUP","REMARKS"])
                            r=cur.fetchall()
                            for x in r:
                                pp2.add_row(x)
                            print(pp2.draw())
                            input('Press Enter to Continue')
                        elif c1==3:
                            break
                elif c==2:
                    p3=Texttable()
                    p3.set_cols_align(['l'])
                    p3.set_cols_valign(['m'])
                    p3.add_rows([['DISPLAY DOCTOR DETAILS'],
                                 ['1. Search Using Patient ID'],
                                 ['2. Search Using Patient Name'],
                                 ['3. Back']
                                 ])
                    while True:
                        print(p3.draw())
                        c2=int(input('Enter Choice: '))
                        if c2==1:
                            q='select patient.name,doctor.name,dept,fees,room from patient,doctor where patient.did=doctor.did and pid=%s'
                            pid=input('Enter Patient ID: ')
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
                        elif c2==2:
                            q='select patient.name,doctor.name,dept,fees,room from patient,doctor where patient.did=doctor.did and patient.name=%s'
                            name=input('Enter Patient Name: ')
                            v=(name,)
                            cur.execute(q,v)
                            pd2=Texttable()
                            pd2.set_cols_align(["c","c","c","c","c"])
                            pd2.set_cols_valign(["m","m","m","m","m"])
                            pd2.set_cols_dtype(["i","t","t","i","i"])
                            pd2.add_row(["PATIENT NAME","DOCTOR NAME","DEPT","FEES","ROOM No."])
                            r=cur.fetchall()
                            for x in r:
                                pd2.add_row(x)
                            print(pd2.draw())
                            input('Press Enter to Continue')

                        elif c2==3:
                            break
                elif c==3:
                    break
        except myc.Error as E:
            print(E.msg)
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
            print(p1.draw())
            c=int(input('Enter Choice: '))
            if c==1:
                q='update login set username=%s where username=%s'
                q1='update patient set pid=%s where pid=%s'
                u=input('Enter New Username: ')
                v=(u,)
                cur.execute(q,v)
                cur.execute(q1,v)
                con.commit()
                print('Username Updated')
            elif c==2:
                q='update login set password=%s where username=%s'
                p=input('Enter New Password: ')
                v=(p,)
                cur.execute(q,v)
                con.commit()
                print('Password Updated')
            elif c==3:
                break
    except myc.Error as E:
        print(E.msg)
