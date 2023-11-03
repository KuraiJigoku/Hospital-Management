
"""
This program is a hospital management system that allows users to login as either an admin or a user. 
Admins can add, remove, update, and display doctor and patient details. 
Users can view patient details. 
"""

from math import e
import management.admin as admin
import management.user as user
from texttable import Texttable

t1 = Texttable()
t1.set_cols_align(['l'])
t1.set_cols_valign(['m'])


t1.add_rows([['WELCOME TO RADCLIFF HOSPITAL MANAGEMENT SYSTEM'],
             ['1. Login as ADMIN'],
             ['2. Login as USER'],
             ['3. Exit']
             ])
while True:
    print(t1.draw())
    v = int(input('Enter your Choice: '))
    if v == 1:
        t=admin.login()
        if t=='True':
            t2 = Texttable()
            t2.set_cols_align(['l'])
            t2.set_cols_valign(['m'])
            t2.add_rows([['LOGGED IN AS ADMIN'],
                         ['1. Doctors Details'],
                         ['2. Patient Details'],
                         ['3. Back']
                         ])
            while True:
                print(t2.draw())

                c = int(input('Enter Choice: '))
                if c == 1: 
                    t3 = Texttable()
                    t3.set_cols_align(['l'])
                    t3.set_cols_valign(['m'])
                    t3.add_rows([['LOGGED IN AS ADMIN'],
                                 ['1. Add Doctor Details'],
                                 ['2. Remove Doctor Details'],
                                 ['3. Update Doctor Details'],
                                 ['4. Display Doctor Details'],
                                 ['5. Back']
                                 ])
                    while True:
                        print(t3.draw())
                        c1 = int(input('Enter Choice: '))
                        if c1 == 1:
                            admin.adoctor()
                            input('Press Enter to Continue')
                        elif c1 == 2:
                            admin.rdoctor()
                            input('Press Enter to Continue')
                        elif c1 == 3:
                            admin.udoctor()
                            input('Press Enter to Continue')
                        elif c1 == 4:
                            admin.ddoctor()
                            input('Press Enter to Continue')
                        elif c1 == 5:
                            break
                elif c == 2:
                    t4 = Texttable()
                    t4.set_cols_align(['l'])
                    t4.set_cols_valign(['m'])
                    t4.add_rows([['LOGGED IN AS ADMIN'],
                                 ['1. Add Patient Details'],
                                 ['2. Remove Patient Details'],
                                 ['3. Update Patient Details'],
                                 ['4. Display Patient Details'],
                                 ['5. Back']
                                 ])
                    while True:
                        print(t4.draw())
                        c1 = int(input('Enter Choice: '))
                        if c1 == 1:
                            admin.apatient()
                            input('Press Enter to Continue')
                        elif c1 == 2:
                            admin.rpatient()
                            input('Press Enter to Continue')
                        elif c1 == 3:
                            admin.upatient()
                            input('Press Enter to Continue')
                        elif c1 == 4:
                            admin.dpatient()
                            input('Press Enter to Continue')
                        elif c1 == 5:
                            break
                elif c == 3:
                    break 
        else:
            print('Invalid Username or Password')
            input('Press Enter to Continue')
    elif v == 2:
        u1=user.login()
        if u1=='True':
            user.dpatient()
        else:
            print('Invalid Username or Password')
            input('Press Enter to Continue')


    elif v == 3:
        print("Exiting...")
        break
