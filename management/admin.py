import myc
from texttable import Texttable
u=input('Enter Admin Username: ')
p=input('Enter Admin Password: ')
con,cur=myc.connection()


def login():
    v=(u,)
    q='select * from login where username=%s'
    cur.execute(q,v)
    t=''
    for x in cur:
        if x[1]==p:
            t='True'
    return t
t=login()
if t=="True":
    print('harry')

