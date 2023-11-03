#This File is only made for automatic insertion of values in the database if needed. It is not required for the program to run.
import mysqlc
import mysql.connector as myc

con,cur=mysqlc.connection()

def audoctor():
    """
    This function creates a table 'doctor' if it doesn't exist and inserts data into it.
    The table has columns 'DID', 'NAME', 'DEPT', 'FEES', 'ROOM', where 'DID' is the primary key.
    """
    try:
        cur.execute('CREATE TABLE IF NOT EXISTS doctor(DID int,NAME varchar(40),DEPT varchar(40),FEES int,ROOM int,PRIMARY KEY (DID))')
        q='insert ignore into doctor values(%s,%s,%s,%s,%s)'
        v = [(101,'Dr A','General Physician',500,1), (102,'Dr B','Audiologist',500,2), (103,'Dr C','Cardiologist',700,3), (104,'Dr D','Neurologist',800,4), (105,'Dr E','Dermatologist',600,5)]
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
        v = [('A','P1','M',25,'A+','Fever',101), ('B','P2','F',20,'B+','Chest Pain',103), ('C','P3','M',30,'O+','Ear issues',102), ('D','P4','F',35,'A+','Cough',101), ('E','P5','M',40,'B+','Skin Disease',105)]
        for x in v:
            pid,name,gender,age,blood,problem,did=x[0],x[1],x[2],x[3],x[4],x[5],x[6]
            v2=pid,name,gender,age,blood,problem,did
            cur.execute(q,v2)
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
