import mysql.connector

mydb=mysql.connector.connect(user='root',host='localhost',passwd='')

mycursor=mydb.cursor()

try:
    mycursor.execute("create database bank")
    mycursor.execute("use bank")
except:
    mycursor.execute("use bank")

print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("++                                                      ++")
print("++                                                      ++")
print("++         Welcome To Banking Management System         ++")
print("++                                                      ++")
print("++                                                      ++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

def Menu():
    print("\n======================= MAIN MENU ========================")
    print("\n1. Insert Record/Records")
    print("\n2. Display Records : ")
    print("  (a). Sorted as per Account Number")
    print("  (b). Sorted as per Customer Name")
    print("  (c). Sorted as per Customer Balance")
    print("\n3. Search Record Details as per the account number")
    print("\n4. Update Record")
    print("\n5. Delete Record")
    print("\n6. Transactions Debit/Withdraw from the account : ")
    print("  (a). Debit/Withdraw from the account")
    print("  (b). Credit into the account")
    print("\n7. Exit")

def MenuSort():
    print("\n a. Sorted as per Account Number")
    print(" b. Sorted as per Customer Name")
    print(" c. Sorted as per Customer Balance")
    print(" d. Back\n")

def MenuTransaction():
    print("")
    print("\n a. Debit/Withdraw from the account")
    print(" b. Credit into the account")
    print(" c. Back\n")

def Create():
    try:
        mycursor.execute('create table bank(ACCNO varchar(10),NAME varchar(50),MOBILE varchar(10),EMAIL varchar(50),ADDRESS varchar(50),CITY varchar(10),COUNTRY varchar(20),BALANCE integer(15))')
        Insert()
    except:
        Insert()

def Insert():
            while True:
              Acc=input("Enter account number : ")
              Name=input("Enter Name : ")
              Mob=input("Enter Mobile number : ")
              email=input("Enter Email : ")
              Add=input("Enter Address : ")
              City=input("Enter City : ")
              Country=input("Enter Country : ")
              Bal=int(input("Enter Balance : "))
              Rec=[Acc,Name.upper(),Mob,email.upper(),Add.upper(),City.upper(),Country.upper(),Bal]
              Cmd="insert into BANK values(%s,%s,%s,%s,%s,%s,%s,%s)"
              mycursor.execute(Cmd,Rec)
              mydb.commit()
              print("\nRecord Inserted.\n")
              break

def Disp(cmd):
    try:
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        print("%15s %15s %15s %15s %15s %15s %15s %15s" % ("ACCNO","NAME","MOBILE","EMAIL ID","ADDRESS","CITY","COUNTRY","BALANCE"))
        print("="*130)
        for i in S:
            for j in i:
                print("%14s" % j, end=' ')
            print()
        print("="*130)
    except:
        print("\nTable doesn't exist.\n")


def DispSortAcc():
    cmd=Disp("select * from BANK order by ACCNO")

def DispSortName():
    cmd=Disp("select * from BANK order by NAME")

def DispSortBal():
    cmd=Disp("select * from BANK order by BALANCE")

def DispSearchAcc(): 
    try:
        mycursor.execute("select * from BANK")
        S=mycursor.fetchall()
        ch=input("\nEnter the account number to be searched : ")
        for i in S:
            if i[0]==ch:
                print("="*130)
                print("%15s %15s %15s %15s %15s %15s %15s %15s" % ("ACCNO","NAME","MOBILE","EMAIL ID","ADDRESS","CITY","COUNTRY","BALANCE"))
                print("="*130)
                for j in i:
                    print('%14s' % j,end=' ')
                print()
                break
        else:
            print("\nRecord Not found.\n")
    except:
        print("\nTable doesn't exist.\n")

def Update(): 
    try:
        mycursor.execute("select * from BANK")
        S=mycursor.fetchall()
        A=input("Enter the account number whose details to be changed : ")
        for i in S:
            i=list(i)
            if i[0]==A:
                ch=input("Change Name(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[1]=input("Enter Name : ")
                    i[1]=i[1].upper()
                ch=input("Change Mobile(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[2]=input("Enter Mobile : ")
                ch=input("Change Email(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[3]=input("Enter email : ")
                    i[3]=i[3].upper()
                ch=input("Change Address(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[4]=input("Enter Address : ")
                    i[4]=i[4].upper()
                ch=input("Change city(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[5]=input("Enter City : ")
                    i[5]=i[5].upper()
                ch=input("Change Country(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[6]=input("Enter country : ")
                    i[6]=i[6].upper()
                ch=input("Change Balance(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[7]=float(input("Enter Balance : "))
                cmd="UPDATE BANK SET NAME=%s,MOBILE=%s,EMAIL=%s,ADDRESS=%s,CITY=%s,COUNTRY=%s,BALANCE=%s WHERE ACCNO=%s"
                val=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print("\nAccount Updated.\n")
                break
        else:
            print("\nRecord not found.\n")
    except:
        print("\nNo such table.\n")

def Delete():
    try:
        mycursor.execute("select * from BANK")
        S=mycursor.fetchall()
        A=input("Enter the account number whose record is to be deleted : ")
        for i in S:
            i=list(i)
            if i[0]==A:
                cmd="delete from bank where accno=%s"
                val=(i[0],)
                mycursor.execute(cmd,val)
                mydb.commit()
                print("\nAccount Deleted.\n")
                break
        else:
            print("\nRecord not found.\n")
    except:
        print("\nNo such Table.\n")

def Debit():
    try:
        mycursor.execute("select * from BANK")
        S=mycursor.fetchall()
        print("\nNOTE : Money can only be debited if minimum balance of Rs.5000 exists.\n")
        acc=input("Enter the account number from which the money is to be withdrawn : ")
        for i in S:
            i=list(i)
            if i[0]==acc:
                Amt=float(input("\nEnter the amount to be withdrawn : "))
                if i[7]-Amt>=5000:
                    i[7]-=Amt
                    cmd="UPDATE BANK SET BALANCE=%s WHERE ACCNO=%s"
                    val=(i[7],i[0])
                    mycursor.execute(cmd,val)
                    mydb.commit()
                    print("\nAmount Debited.\n")
                    break
                else:
                    print("\nThere must be min balance of Rs 5000.\n")
                    break
        else:
            print("\nRecord Not found.\n")
    except:
        print("\nTable Doesn't exist.\n")

def Credit():
    try:
        mycursor.execute("select * from BANK")
        S=mycursor.fetchall()
        acc=input("\nEnter the account number in which the money is to be credited : ")
        for i in S:
            i=list(i)
            if i[0]==acc:
                Amt=float(input("\nEnter the amount to be credited : "))
                i[7]+=Amt
                cmd="UPDATE BANK SET BALANCE=%s WHERE ACCNO=%s"
                val=(i[7],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print("\nAmount Credited.\n")
                break
        else:
            print("\nRecord Not found.\n")
    except:
        print("\nTable Doesn't exist.\n")

while True:
    Menu()
    ch=input("\nEnter your Choice : ")
    if ch=="1":
        Create()
    elif ch=="2":
        while True:
            MenuSort()
            ch1=input("\nEnter choice [a/b/c/d] : ")
            print("")
            if ch1 in ['a','A']:
                DispSortAcc()
            elif ch1 in ['b','B']:
                DispSortName()
            elif ch1 in ['c','C']:
                DispSortBal()
            elif ch1 in ['d','D']:
                print("\nBack to the main menu.\n")
                break
            else:
                print("\nInvalid choice.\n")
    elif ch=="3":
        DispSearchAcc()
    elif ch=="4":
        Update()
    elif ch=="5":
        Delete()
    elif ch=="6":
        while True:
            MenuTransaction()
            ch1=input("\nEnter choice [a/b/c] : ")
            if ch1 in ['a','A']:
                Debit()
            elif ch1 in ['b','B']:
                Credit()
            elif ch1 in ['c','C']:
                print("\nBack to the main menu.\n")
                break
            else:
                print("\nInvalid choice.\n")
    elif ch=="7":
        print("\nExiting...".center(75))
        print("\nThank you ! Have a nice day .\n")
        break
    else:
        print("\nInvalid choice.\n")
