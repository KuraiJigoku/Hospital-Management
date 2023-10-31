import prequisite
import management.admin as admin
from texttable import Texttable
t=Texttable()
t.set_cols_align(['c'])
t.set_cols_valign(['m'])
t.add_rows([['WELCOME TO RADCLIFF HOSPITAL MANAGEMENT SYSTEM'],
            ['1. Login as ADMIN'],
            ['2. Register as USER'],
            ['3. Login as User']
            ])
t.draw()
v=int(input('Enter your Choice: '))
if v==1:
    t=Texttable()
    t.set_cols_align(['c'])
    t.set_cols_valign(['m'])
    t.add_rows([['LOGGED IN AS ADMIN'],
                ['1. Add Doctors'],
                ['2. Update Patient'],
                ['3. Login as User']
                ])
    t.draw()
    c=int(input('Enter Choice: '))
    
