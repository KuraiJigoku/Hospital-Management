import mysql.connector as myc
host=input('Enter MySQL server hostname: ')
user=input('Enter MySQL Username: ')
pas=input('Enter MySQL Password: ')

def connection():
    try:
        con=myc.connect(host=host,user=user,password=pas)
        cur=con.cursor()
        print('Connection Successfull')
        cur.execute("USE xiiproject")
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
             cur.execute("CREATE DATABASE IF NOT EXISTS xiiproject")
        cur.execute("USE xiiproject")
    except myc.Error as E:
        print(E.msg)