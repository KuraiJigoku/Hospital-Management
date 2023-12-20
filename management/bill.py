import mysqlc
con,cur=mysqlc.connection()
from texttable import Texttable
# Function to add bill for a patient
def abill(pid,did):
    cur.execute('CREATE TABLE IF NOT EXISTS appointments(APPOINTMENT_ID int, PID varchar(15), DID int, APPOINTMENT_FEE decimal(10,2), PRIMARY KEY (APPOINTMENT_ID), FOREIGN KEY (PID) references patient(PID), FOREIGN KEY (DID) references doctor(DID))')
    appointment_id = input('Enter Appointment ID: ')
    cur.execute('select fees from doctor where did=%s', (did,))
    appointment_fee = 0
    for x in cur:
        appointment_fee = x[0]
    q = 'insert ignore into appointments values(%s,%s,%s,%s)'
    v = (appointment_id, pid, did, appointment_fee)
    cur.execute(q, v)
    con.commit()
    q1 = 'select * from appointments where appointment_id=%s'
    v1 = (appointment_id,)
    cur.execute(q1, v1)
    t8 = Texttable()
    t8.set_cols_align(["c", "c", "c", "c"])
    t8.set_cols_valign(["m", "m", "m", "m"])
    t8.set_cols_dtype(["i", "t", "i", "i"])
    t8.add_row(["APPOINTMENT_ID", "PID", "DID", "APPOINTMENT_FEE"])
    r = cur.fetchall()
    for x in r:
        t8.add_row(x)
    print(t8.draw())

    print('Appointment Bill Added Successfully')