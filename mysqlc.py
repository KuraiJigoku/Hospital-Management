
import mysql.connector as myc
host=input('Enter MySQL server hostname: ')
user=input('Enter MySQL Username: ')
pas=input('Enter MySQL Password: ')

def connection():
    """
    Establishes a connection to the MySQL server and creates a database if it doesn't exist.
    Returns a tuple containing the connection and cursor objects.
    """
    try:
        con=myc.connect(host=host,user=user,password=pas)
        cur=con.cursor()
        print('Connection Successfull')
        cur.execute("CREATE DATABASE IF NOT EXISTS xiiproject1")
        cur.execute("USE xiiproject1")
        print('Connected to Database')
        return con,cur
    except myc.Error as E:
        print(E.msg)