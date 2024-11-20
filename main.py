import mysql.connector
import re
from tabulate import tabulate
import datetime
import time
import sys
from os import system
connect_1 = mysql.connector.connect(user='root',passwd='My_Local_Host@2213', database='finderr')
curs = connect_1.cursor() # initialize cursor
# regular expressions

# Essential functions
def ptype(alpha):
    for i in alpha:
        print(i,end='')
        time.sleep(0.05)
    print()
def validate_phone(phone_no):
    phone_pattern = r'^\d{10}$' # regex pattern
    if not re.match(phone_pattern, phone_no):
        raise ValueError("\033[31mInvalid phone number. Please enter a 10-digit phone number.\033[0m")
    else:
        pass
def match_rate(sub,sup):
    count = 0
    for i in sub:
        if i in sup:
            count+=1
    return (count/len(sub)) * 100
# ------- sections -------
def newbee(name):
    ptype(f'Hello {name} !')
    ptype('We would like to get some quick details from you ! Don\'t worry it is up to you whether you want to make these details public or private :)')
    ptype(f'{name} please tell us about your address ...')
    address = input('Enter address : ')
    ptype(f'{name} do you want this address to be visible to other users ? (yes/no) ')
    choice = input()
    if(choice == 'no'.lower()):
        public_address = "None"
    else:
        public_address = address
    ptype('Thank you for your time ! You may now proceed to the next section ...')
    return address,public_address

def services():
    
    
    m=0
    def cmd1():
        search_surname=input("Enter the surname of the person you want to search for : ")
        query="select first_name,last_name,email,phone_no,public_address from users where last_name=%s"
        tupple=(search_surname,)
        curs.execute(query,tupple)
        resultset=curs.fetchall()
        new_reslist=[]#in order to add all the elements of resultset into the list
        for i in resultset:
            new_reslist.append(i)#[(...,...),(...,...),...]
        print(tabulate(new_reslist,headers=("Goodname","Surname","Email","Phone Number","Address"),tablefmt='pretty'))

    def cmd2():
        search_name=input("Enter the good name of the person you want to search for : ")
        query="select first_name,last_name,email,phone_no,public_address from users where first_name=%s"
        tupple=(search_name,)
        curs.execute(query,tupple)
        resultset=curs.fetchall()
        new_reslist=[]#in order to add all the elements of resultset into the list
        for i in resultset:
            new_reslist.append(i)#[(...,...),(...,...),...]   
        print(tabulate(new_reslist,headers=("Goodname","Surname","Email","Phone Number","Address"),tablefmt='pretty'))

    def cmd3():
        search_phone=input("Enter the phone number of the person you want to search for : ")
        query="select first_name,last_name,email,phone_no,public_address from users where phone_no=%s"
        tupple=(search_phone,)
        curs.execute(query,tupple)
        resultset=curs.fetchall()
        new_reslist=[]#in order to add all the elements of resultset into the list
        for i in resultset:
            new_reslist.append(i)#[(...,...),(...,...),...]  
        print(tabulate(new_reslist,headers=("Goodname","Surname","Email","Phone Number","Address"),tablefmt='pretty'))

    def cmd4():
        search_email=input("Enter the email of the person you want to search for : ")
        query="select first_name,last_name,email,phone_no,public_address from users where email=%s"
        tupple=(search_email,)
        curs.execute(query,tupple)
        resultset=curs.fetchall()
        new_reslist=[]#in order to add all the elements of resultset into the list
        for i in resultset:
            new_reslist.append(i)#[(...,...),(...,...),...]  
        print(tabulate(new_reslist,headers=("Goodname","Surname","Email","Phone Number","Address"),tablefmt='pretty'))

    def cmd5():
        search_address=input("Enter the address of the person you want to search for : ")
        try:
            # query="select first_name,last_name,email,phone_no,public_address from users where public_address=%s"
            query = "select first_name,last_name,email,phone_no,public_address from users;"
            # tupple=(search_address,)
            curs.execute(query)
            resultset=curs.fetchall()
            # print(resultset)
            new_reslist=[]#in order to add all the elements of resultset into the list
            for i in resultset:
                # print(match_rate(search_address,i[0]))
                # print(i)
                if(match_rate(search_address,i[4])>=80):
                    # print(i[0])
                    new_reslist.append(i)#[(...,...),(...,...),...] 
            # for i in resultset:
            print(tabulate(new_reslist,headers=("Goodname","Surname","Email","Phone Number","Address"),tablefmt='pretty'))
            print("")
            print("NOTE :- If no data appears then it might be possible that the address inputted may not be correct or the person might not have registered their address")
        except:
            print("Appologies, No Such Address Found !")
    # ----------------------------- VIMP -----------------------------
    def cmd6():
        global u_email
        global u_pwd
        query="select first_name,last_name,email,phone_no,public_address from users where email=%s and password=%s"#q-query for importing user details
        tup=(u_email,u_pwd)
        curs.execute(query,tup)
        resultset=curs.fetchone()
        print("Your Inputted Details :-")
        print(tabulate([resultset],headers=("Goodname","Surname","Email","Phone Number","Address"),tablefmt='pretty'))
        print("USER OPERATIONS :-")
        print("A. To modify name...")
        print("B. To modify surname...")
        print("C. To modify email...")
        print("D. To modify password...")
        print("E. To modify phone number...")
        print("F. To modify address...")
        user_cmd=input("Enter operation:")
        if user_cmd=="A":
            print("User Operation :- To modify name...")
            name=input("Enter updated name:")
            query='''update users set first_name=%s where email=%s'''
            value=(name,u_email)
            curs.execute(query,value)
            connect_1.commit()
            print("Done")
            query2='''select * from users where email=%s'''
            vals=(u_email,)
            curs.execute(query2,vals)
            mydata=curs.fetchone()
            print('Updated good name !')

        elif user_cmd=="B":
            print("User Operation :- To modify surname...")
            ask_surname=input("Enter updated surname:")
            query='''update users set last_name=%s where email=%s'''
            value=(ask_surname,u_email)
            curs.execute(query,value)
            connect_1.commit()
            print("Done")
            query2='''select * from users where Email=%s'''
            vals=(u_email,)
            curs.execute(query2,vals)
            mydata=curs.fetchone()
            print('Updated surname !')

        elif user_cmd=="C":
            print("User Operation :- To modify email...")
            email=input("Enter updated email:")
            query='''update users set email=%s where email=%s'''
            value=(email,u_email)
            curs.execute(query,value)
            connect_1.commit()
            print("Done")
            u_email = email
            query2='''select * from users where email=%s'''
            vals=(u_email,)
            curs.execute(query2,vals)
            mydata=curs.fetchone()
            print(mydata)

        elif user_cmd=="D":
            print("User Operation :- To modify password...")
            ask_password=input("Enter updated password:")
            query='''update users set Password=%s where Email=%s'''
            value=(ask_password,u_email)
            curs.execute(query,value)
            connect_1.commit()
            u_pwd = ask_password # update password
            print("Updated password !")

        elif user_cmd=="E":
            print("User Operation :- To modify phone number ...")
            ask_phone=input("Enter updated phone number : ")
            query='''update users set phone_no=%s where Email=%s'''
            value=(ask_phone,u_email)
            curs.execute(query,value)
            connect_1.commit()
            print("Updated phone number !")
            # query2='''select * from users where email=%s'''
            # vals=(u_email,)
            # curs.execute(query2,vals)
            # mydata=curs.fetchone()
            # print(mydata)
        elif user_cmd=="F":
            print("User Operation :- To modify address...")
            final_address=input("Enter updated address:")
            ptype('Update public address also ? (yes/no) ')
            choice = input()
            if(choice == 'yes'.lower()):
                public_address = final_address
            else:
                public_address = 'None'
            query='''update users set address = %s, public_address = %s where email=%s'''
            value=(final_address,public_address,u_email)
            curs.execute(query,value)
            connect_1.commit()
            print("Done")
            query2='''select * from users where Email=%s'''
            vals=(u_email,)
            curs.execute(query2,vals)
            mydata=curs.fetchone()
            print(mydata)   
    def cmd7():
        global u_email
        global u_pwd
        query = "select first_name,last_name,email,password,phone_no,address,public_address from users where email = %s and password = %s;"
        tup=(u_email,u_pwd)
        curs.execute(query,tup)
        resultset=curs.fetchone()
        print("Your Inputted Details :-")
        print(tabulate([resultset],headers=("Goodname","Surname","Email","Password","Phone Number","Address","Public Address"),tablefmt='pretty'))

    def cmd8():
        global u_email
        global u_pwd
        ptype("Caution: Your record will be completely deleted from the directory along with your details ...")
        choice=input("Do you want to proceed with this operation (Yes/No):")
        if choice == 'yes'.lower():
            query="delete from users where email=%s;"#q-query for importing user details
            tup=(u_email,)
            curs.execute(query,tup)
            ptype("Your Record Has Been Deleted !")
            time.sleep(2)
            exec(open(sys.argv[0]).read()) # re-execute the program
        else:
            ptype('No worries :)')
    while(True):
        print("\033[1m\033[35m-- Finderr --\033[0m")
        print("\033[1mMENU OPERATIONS :-")
        print("1. Search a person by surname ...")
        print("2. Search a person by name ...")
        print("3. Search a person by phone number ...")
        print("4. Search a person by email ...")
        print("5. Search a person by address ...")
        print("6. Modify your inputted details ...")
        print("7. View your inputted data ...")
        print("8. Delete your record permanently ...")
        print("9. Quit the session ...")
        print("")
        print('''Note :- 1. In order to display menu operations in work space type: "_menu".
            2. If no data appears then it might be possible that the inputted details are wrong or the person have not registered.\033[0m''')
        # all operations start now
        print('-----------------------------------')
        cmd = int(input('Enter command : '))
        print('-----------------------------------')
        if(cmd == 1):
            ptype('Let\'s search people based on their surname ...')
            cmd1()
        elif(cmd == 2):
            ptype('Let\'s search people based on their good name ...')
            cmd2()
        elif(cmd == 3):
            ptype('Let\'s search people based on their phone number ...')
            cmd3()
        elif(cmd == 4):
            ptype('Let\'s search people based on their email ...')
            cmd4()
        elif(cmd == 5):
            ptype('Let\'s search people based on their address ...')
            cmd5()
        elif(cmd == 6):
            cmd6()
        elif(cmd == 7):
            ptype('Displaying your profile ...')
            cmd7()
        elif(cmd == 8):
            cmd8()
        elif(cmd == 9):
            ptype("Made with love by Devansh Rathore 🥰 ❣ 💓 ❥ 💜")
            time.sleep(5)
            sys.exit(0)
def validate_email(email):
    # regex pattern
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if not re.match(email_pattern, email):
        raise ValueError("\033[31mInvalid email address. Please enter a valid email.\033[0m")
    else:
        pass


# __main__ segment
# --  run automatically --
curs.execute('delete from users;')
q = "insert into users (phone_no,first_name,last_name,email,password,address,public_address) values(\"9878100224\",\"Devansh\",\"Rathore\",\"devr211@gmail.com\",\"Dimsums2211\",\"Vishali, Jaipur\",\"Vishali, Jaipur\");"
curs.execute(q)
q = "insert into users (phone_no,first_name,last_name,email,password,address,public_address) values(\"9868017743\",\"Vijay\",\"Thalapathy\",\"vijayr@gmail.com\",\"Dimsums2211\",\"Vaishali, Jaipur\",\"Vaishali, Jaipur\");"
curs.execute(q)
q = "insert into users (phone_no,first_name,last_name,email,password,address,public_address) values(\"9675323345\",\"Rana\",\"Rathore\",\"ranar212@gmail.com\",\"Dimsums2211\",\"Vidya Mandir, Jaipur\",\"Bagru, Jaipur\");"
curs.execute(q)
connect_1.commit()
q="select * from users;"
searchset=[]
curs.execute(q)
searchset=curs.fetchall()
# print(searchset)
# u_email = 'devr211@gmail.com'
# u_pwd = 'Dimsums2211'
# --- login/signup ---
print('1. New User')
print('2. Existing User')
choice = int(input('Enter choice : '))
if(choice == 1):
    print('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-')
    ptype('Welcome to \033[1m\033[35mFinderr\033[0m')
    print('Enter your details ...')
    u_name = input('Name : ')
    while(True): #validate phone number
        try:
            u_phNo = input('Phone number : ')
            # validate_phone(u_phNo)
            # check for existance in searchset
            if u_phNo == searchset[0][1]:
                raise ValueError("\033[31mSorry to interupt but you might have entered a wrong phone number as it aldready exists in the record !\033[0m")
            break
        except ValueError as err:
            print(err)
    u_pwd = input('Password : ')
    while(True): #validate email
        try:
            u_email = input('Email : ')
            # validate_email(u_email)
            break
        except ValueError as err:
            print(err)
    # dbms operation
    l = u_name.split()
    fname,lname = l[0],l[1]
    q="insert into users (phone_no,first_name,last_name,email,password,address,public_address) values (%s,%s,%s,%s,%s,%s,%s);"
    val=(u_phNo,fname,lname,u_email,u_pwd,) + newbee(fname)
    curs.execute(q,val)
    connect_1.commit()
    # print(searchset)


elif choice == 2:
    print('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-')
    ptype('Enter your details ...')
    while(True): #validate phone number
        try:
            u_phNo = input('Phone number : ')
            # validate_phone(u_phNo)
            break
        except ValueError as err:
            print(err)
    u_pwd = input('Password : ')
    q="select first_name,last_name,email,password,phone_no,address,public_address from users where phone_no=%s and password=%s"#q-query for importing user details
    val=(u_phNo,u_pwd)
    curs.execute(q,val)
    searchset=curs.fetchone()
    # print(searchset)
    if (u_pwd != None and u_phNo != None):
        print("Successfuly logged in !")
        ptype(f"Hello {searchset[0]} !")
        print("Type '_details' to check your details")
        x=input()#for checking details
        #x="_details" 
        if x=="_details":
            time.sleep(1)
            print(tabulate([searchset], headers=("Good Name","Surname","Email","Password","Phone Number","Address"),tablefmt='pretty'))
            print("")
            print("-- Logged in at",datetime.datetime.now())
    else:
        print('Sorry, couldn\'t recognize you :(')
        exec(open(sys.argv[0]).read()) # re-execute the program
ptype('\033[32mRedirecting you to the main page ...\033[0m')
system("cls")
services()
