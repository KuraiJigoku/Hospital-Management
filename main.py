import prequisite
import management.admin as admin
from texttable import Texttable
t1=Texttable()
t1.set_cols_align(['l'])
t1.set_cols_valign(['m'])
t1.add_rows([['WELCOME TO RADCLIFF HOSPITAL MANAGEMENT SYSTEM'],
             ['1. Login as ADMIN'],
             ['2. Register as USER'],
             ['3. Login as USER']
             ])
print(t1.draw())
v=int(input('Enter your Choice: '))
if v==1:
    t2=Texttable()
    t2.set_cols_align(['l'])
    t2.set_cols_valign(['m'])
    t2.add_rows([['LOGGED IN AS ADMIN'],
                 ['1. Doctors Details'],
                 ['2. Patient Details'],
                 ['3. Exit']
                 ])
    print(t2.draw())
    c=int(input('Enter Choice: '))
    
