import mysql.connector as myc
host=input('Enter MySQL server hostname: ')
user=input('Enter MySQL Username: ')
pas=input('Enter MySQL Password: ')

def connection():
    try:
        con=myc.connect(host=host,user=user,password=pas)
        cur=con.cursor()
        print('Connection Successfull')
        return con,cur
    except myc.Error as E:
        print(E.msg)
def create(cur):
    try:

        cur.execute("SHOW DATABASES")
        temp = cur.fetchall()
        databases=[]
        for x in temp:
             databases.append(x)
        if "xiiproject" not in databases:
             cur.execute("CREATE DATABASE xiiproject")
        cur.execute("USE xiiproject")
        cur.execute('CREATE TABLE doctor(DID int,NAME varchar(20),DEPT varchar(20),FEES int,ROOM int,PRIMARY KEY (DID))')
        cur.execute('CREATE TABLE login(USERNAME varchar(15),PASSWORD varchar(20),ROLE varchar(10))')
        cur.execute('CREATE TABLE patient(PID int,USERNAME varchar(15),NAME varchar(20),AGE int,BLOOD_GROUP varchar(3),DID int,PRIMARY KEY (PID),FOREIGN KEY (DID) references doctor(DID)),FOREIGN KEY (USERNAME) references login(USERNAME))')
    except myc.Error as E:
        print(E.msg)