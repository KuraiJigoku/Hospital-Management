import management.admin as admin
from texttable import Texttable

t1 = Texttable()
t1.set_cols_align(['l'])
t1.set_cols_valign(['m'])

while True:
    t1.add_rows([['WELCOME TO RADCLIFF HOSPITAL MANAGEMENT SYSTEM'],
                 ['1. Login as ADMIN'],
                 ['2. Register as USER'],
                 ['3. Login as USER'],
                 ['4. Exit']
                 ])
    print(t1.draw())
    v = int(input('Enter your Choice: '))
    if v == 1:
        while True:
            t=admin.login()
            if t == 1:
                while True:
                    t2 = Texttable()
                    t2.set_cols_align(['l'])
                    t2.set_cols_valign(['m'])
                    t2.add_rows([['LOGGED IN AS ADMIN'],
                                 ['1. Doctors Details'],
                                 ['2. Patient Details'],
                                 ['3. Exit']
                                 ])
                    print(t2.draw())
                    c = int(input('Enter Choice: '))
                    if c == 1:
                        while True:
                            t2 = Texttable()
                            t2.set_cols_align(['l'])
                            t2.set_cols_valign(['m'])
                            t2.add_rows([['LOGGED IN AS ADMIN'],
                                         ['1. Add Doctor Details'],
                                         ['2. Remove Doctor Details'],
                                         ['3. Update Doctor Details'],
                                         ['4. Display Doctor Details'],
                                         ['5. Exit']
                                         ])
                            print(t2.draw())
                            c1 = int(input('Enter Choice: '))
                            if c1 == 1:
                                admin.adoctor()
                            elif c1 == 2:
                                admin.rdoctor()
                            elif c1 == 3:
                                admin.udoctor()
                            elif c1 == 4:
                                admin.ddoctor()
                            elif c1 == 5:
                                break
                    elif c == 2:
                        while True:
                            t2 = Texttable()
                            t2.set_cols_align(['l'])
                            t2.set_cols_valign(['m'])
                            t2.add_rows([['LOGGED IN AS ADMIN'],
                                         ['1. Add Patient Details'],
                                         ['2. Remove Patient Details'],
                                         ['3. Update Patient Details'],
                                         ['4. Display Patient Details'],
                                         ['5. Exit']
                                         ])
                            print(t2.draw())
                            c1 = int(input('Enter Choice: '))
                            if c1 == 1:
                                admin.apatient()
                            elif c1 == 2:
                                admin.rpatient()
                            elif c1 == 3:
                                admin.upatient()
                            elif c1 == 4:
                                admin.dpatient()
                            elif c1 == 5:
                                break
                    elif c == 3:
                        break
            elif v == 2:
                while True:
                    t2 = Texttable()
                    t2.set_cols_align(['l'])
                    t2.set_cols_valign(['m'])
                    t2.add_rows([['REGISTER AS USER'],
                         ['1. Add User Details'],
                         ['2. Remove User Details'],
                         ['3. Update User Details'],
                         ['4. Display User Details'],
                         ['5. Exit']
                         ])
                print(t2.draw())
                c1 = int(input('Enter Choice: '))
                if c1 == 1:
                    admin.auser()
                elif c1 == 2:
                    admin.ruser()
                elif c1 == 3:
                    admin.uuser()
                elif c1 == 4:
                    admin.duser()
                elif c1 == 5:
                    break
            elif v == 3:
                print("User login is not implemented yet")
            elif v == 4:
                print("Exiting...")
                break

           

