#This File is only made for automatic insertion of values in the database if needed. It is not required for the program to run.
import mysqlc
import mysql.connector as myc
import management.bill as bill

con,cur=mysqlc.connection()

def audoctor():
    """
    This function creates a table 'doctor' if it doesn't exist and inserts data into it.
    The table has columns 'DID', 'NAME', 'DEPT', 'FEES', 'ROOM', where 'DID' is the primary key.
    """
    try:
        cur.execute('CREATE TABLE IF NOT EXISTS doctor(DID int,NAME varchar(40),DEPT varchar(40),FEES int,ROOM int,PRIMARY KEY (DID))')
        q='insert ignore into doctor values(%s,%s,%s,%s,%s)'
        v = [(101,'Dr. Gregory House','Diagnostic Medicine',500,1), (102,'Dr. James Wilson','Oncologist',500,2), (103,'Dr. Allison Cameron','Immunologist',700,3), (104,'Dr. Robert Chase','Surgeon',800,4), (105,'Dr. Eric Foreman','Neurologist',600,5)]
        for x in v:
            did,name,dept,fees,room=x[0],x[1],x[2],x[3],x[4]
            v1=did,name,dept,fees,room
            cur.execute(q,v1)
            con.commit()
        print('Added Doctors Successfully')
    except myc.Error as E:
        print(E.msg)

audoctor()

def aupatient():
    """
    This function creates a table 'patient' if it doesn't exist and inserts data into it.
    The table has columns 'PID', 'NAME', 'GENDER', 'AGE', 'BLOOD_GROUP', 'REMARK', 'DID', where 'PID' is the primary key and 'DID' is a foreign key referencing 'DID' from the 'doctor' table.
    """
    try:
        cur.execute('CREATE TABLE IF NOT EXISTS patient(PID varchar(15),NAME varchar(40),GENDER varchar(10),AGE int,BLOOD_GROUP varchar(5),REMARK varchar(70),DID int,PRIMARY KEY (PID),FOREIGN KEY (DID) references doctor(DID))')
        q='insert ignore into patient values(%s,%s,%s,%s,%s,%s,%s)'
        v = [('10001','Jack','M',25,'A+','Fever',101), ('10002','Peter','F',20,'B+','Chest Pain',101), ('10003','Annie','M',30,'O+','Leukemia',102), ('10004','Aashish','F',35,'A+','Asthma',103), ('10005','Kevin','M',40,'B+','Skin Disease',105)]
        cur.execute('CREATE TABLE IF NOT EXISTS appointments(APPOINTMENT_ID int, PID varchar(15), DID int, APPOINTMENT_FEE decimal(10,2), PRIMARY KEY (APPOINTMENT_ID), FOREIGN KEY (PID) references patient(PID), FOREIGN KEY (DID) references doctor(DID))')
        for x in v:
            pid,name,gender,age,blood,problem,did=x[0],x[1],x[2],x[3],x[4],x[5],x[6]
            v2=pid,name,gender,age,blood,problem,did
            cur.execute(q,v2)
            
            appointment_id=1
            cur.execute('select fees from doctor where did=%s', (did,))
            appointment_fee = 0
            for x in cur:
                appointment_fee = x[0]
            q = 'insert ignore into appointments values(%s,%s,%s,%s)'
            v = (appointment_id, pid, did, appointment_fee)
            cur.execute(q, v)
            con.commit()
            appointment_id+=1
        cur.execute("insert into login values(%s,%s,'USER')",(pid,pid))
        con.commit()
        print('Added Patients Successfully')
        
    except myc.Error as E:
        print(E.msg)

def aulogin():
    """
    This function creates a table 'login' if it doesn't exist and inserts data into it.
    The table has columns 'USERNAME', 'PASSWORD', 'ROLE', where 'USERNAME' is the primary key.
    """
    try:
        cur.execute('CREATE TABLE IF NOT EXISTS login(USERNAME varchar(15),PASSWORD varchar(20),ROLE varchar(10),PRIMARY KEY (USERNAME))')
        cur.execute("insert ignore into login values('admin','radcliff','ADMIN')")
        con.commit()
    except myc.Error as E:
        print(E.msg)

aulogin()
aupatient()
