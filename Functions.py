'''
This File Contains ALL THE FUNCTIONS REQUIRED FOR HOSPITAL MANAGEMENT USING MYSQL DATABASE SYSTEM
'''


import mysql.connector as m
import os
import tabulate
file=m.connect(host='localhost',user='root',password="",database="HOSPITAL")
b=file.cursor()
def add_record():
    print("1. Add DOCTOR's details\n2. Add Patient details")
    ch=int(input("Enter Choice: "))
    if ch==1:
        y=int(input("Enter ID: "))
        b.execute("select * from doctor where ID='{}'".format(y))
        data=b.fetchall()
        if data==[]:
            name=input("Enter name: ")
            q=int(input("Enter Salary: "))
            p=input("Enter Specialization: ")
            b.execute("insert into doctor values('{}','{}','{}','{}')".format(name,y,q,p))
            file.commit()
            print("\t\t-------------------RECORD ADDED SUCCESSFULLY----------------")
        else:
            print("\t\t------------ID ALREADY EXISTS-----------")
    elif ch==2:
        y=int(input("Enter ID: "))
        b.execute("select * from patient where ID='{}'".format(y))
        data=b.fetchall()
        if data==[]:
            name=input("Enter name: ")
            disease=input("Enter disease: ")
            date=input("Enter Admission date: ")
            address=input("Enter Address: ")
            b.execute("insert into patient values('{}','{}','{}','{}','{}')".format(name,y,disease,date,address))
            file.commit()
            print("\t\t-------------------RECORD ADDED SUCCESSFULLY----------------")
        else:
            print("\t\t------------ID ALREADY EXISTS-----------")
def search_record():
    print("1. Search DOCTOR Details\n2. Search Patient Details")
    ch=int(input("Enter Choice: "))
    if ch==1:
        print("1. Search by Name\n2. Search by ID")
        choice=int(input("Enter choice: "))
        if choice==1:
            name=input("Enter Doctor's Name: ")
            b.execute("select * from doctor where name='{}'".format(name))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t---------------NO SUCH RECORD FOUND!!!---------------")
            else:
                print("\t\t\t------------DOCTOR Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Salary','Specialization'],tablefmt='pretty'))
        elif choice==2:
            ID=input("Enter Doctor's ID: ")
            b.execute("select * from doctor where id='{}'".format(ID))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t---------------NO SUCH RECORD FOUND!!!---------------")
            else:
                print("\t\t\t------------DOCTOR Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Salary','Specialization'],tablefmt='pretty'))
        else:
            print("\t\t----------INVALID INPUT!!!--------")
    elif ch==2:
        print("1. Search by Name\n2. Search by ID")
        choice=int(input("Enter choice: "))
        if choice==1:
            name=input("Enter Patient's Name: ")
            b.execute("select * from patient where name='{}'".format(name))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t---------------NO SUCH RECORD FOUND!!!---------------")
            else:
                print("\t\t\t------------Patient Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Disease','Date_Admitted','Address'],tablefmt='pretty'))
        elif choice==2:
            ID=input("Enter Patient's ID: ")
            b.execute("select * from patient where id='{}'".format(ID))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t---------------NO SUCH RECORD FOUND!!!---------------")
            else:
                print("\t\t\t------------PATIENT Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Disease','Date_Admitted','Address'],tablefmt='pretty'))
        else:
            print("\t\t----------INVALID INPUT!!!--------")
    else:
        print("\t\t----------INVALID INPUT!!!--------")
def delete_record():
    print("1. Delete Doctor Records\n2. Delete Patient Records")
    ch=int(input("Enter Choice: "))
    if ch==1:
        print("1. Delete by Name\n2. Delete by ID")
        choice=int(input("Enter choice: "))
        if choice==1:
            name=input("Enter Doctor's Name: ")
            b.execute("select * from doctor where name='{}'".format(name))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t---------------NO SUCH RECORD FOUND!!!---------------")
            else:
                print("\t\t\t------------DOCTOR Records-------")
                for i in data:
                    print(tabulate.tabulate([i],headers=['Name','ID','Salary','Specialization'],tablefmt='pretty'))
                    x=input("Press Y to delete this record: ")
                    if x.upper()=='Y':
                        b.execute("insert into restore_doctor values('{}','{}','{}','{}')".format(i[0],i[1],i[2],i[3]))
                        b.execute("delete from doctor where ID='{}'".format(i[1]))
                        print("\t\t\t---------RECORD DELETED--------")
                        file.commit()
                        break
        elif choice==2:
            ID=input("Enter Doctor's ID: ")
            b.execute("select * from doctor where id='{}'".format(ID))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t---------------NO SUCH RECORD FOUND!!!---------------")
            else:
                print("\t\t\t------------DOCTOR Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Salary','Specialization'],tablefmt='pretty'))
                x=input("Press Y to delete this record: ")
                if x.upper()=='Y':
                    b.execute("insert into restore_doctor values('{}','{}','{}','{}')".format(data[0][0],data[0][1],data[0][2],data[0][3]))
                    b.execute("delete from doctor where ID='{}'".format(ID))
                    print("\t\t\t---------RECORD DELETED--------")
                    file.commit()
        else:
            print("\t\t----------INVALID INPUT!!--------")
    elif ch==2:
        print("1. Delete by Name\n2. Delete by ID")
        choice=int(input("Enter choice: "))
        if choice==1:
            name=input("Enter Patient's Name: ")
            b.execute("select * from patient where name='{}'".format(name))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t---------------NO SUCH RECORD FOUND!!!---------------")
            else:
                print("\t\t\t------------PATIENT Records-------")
                for i in data:
                    print(tabulate.tabulate([i],headers=['Name','ID','Disease','Date_Admitted','Address'],tablefmt='pretty'))
                    x=int(input("Press Y to delete this record: "))
                    if x.upper()=='Y':
                        b.execute("insert into restore_patient values('{}','{}','{}','{}','{}')".format(i[0],i[1],i[2],i[3],i[4]))
                        b.execute("delete from doctor where ID='{}'".format(i[1]))
                        print("\t\t\t---------RECORD DELETED--------")
                        file.commit()
                        break
        elif choice==2:
            ID=input("Enter Patient's ID: ")
            b.execute("select * from Patient where id='{}'".format(ID))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t---------------NO SUCH RECORD FOUND!!!---------------")
            else:
                print("\t\t\t------------PATIENT Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Disease','Date_Admitted','Address'],tablefmt='pretty'))
                x=input("Press Y to delete this record: ")
                if x.upper()=='Y':
                    b.execute("insert into restore_patient values('{}','{}','{}','{}','{}')".format(data[0][0],data[0][1],data[0][2],data[0][3],data[0][4]))
                    b.execute("delete from patient where ID='{}'".format(ID))
                    print("\t\t\t---------RECORD DELETED--------")
                    file.commit()
        else:
            print("\t\t----------INVALID INPUT!!--------")
    else:
        print("\t\t----------INVALID INPUT!!--------")

def update_record():
    print("1. Update Doctor details\n2. Update Patient Details")
    ch=int(input("Enter Choice: "))
    if ch==1:
        print("1. Find record using Doctor's name\n2. Find record using Doctor's ID")
        choice=int(input("Enter choice: "))
        if choice==1:
            name=input("Enter Name: ")
            b.execute("select * from doctor where Name='{}'".format(name))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t----------NO RECORD FOUND!!  -------")
            else:
                for i in data:
                    print(tabulate.tabulate([i],headers=['Name','ID','Salary','Specialization'],tablefmt='pretty'))
                    c=input("Press Y to alter this record: ")
                    if c.upper()=='Y':
                        print("1. Update Name\n2. Update ID\n3. Update All details")
                        d=int(input("Enter choice:"))
                        if d==1:
                            n=input("Enter New Name: ")
                            b.execute("update doctor set Name='{}' where ID='{}'".format(n,i[1]))
                            print("\t\t\t-----------------RECORD HAS BEEN SUCCESSFULLY UPDATED---------------")
                            file.commit()
                            break
                        elif d==2:
                            n=input("Enter New ID: ")
                            b.execute("select * from doctor where ID='{}'".format(n))
                            data1=b.fetchall()
                            if data1==[]:
                                b.execute("update doctor set ID='{}' where ID='{}'".format(n,i[1]))
                                print("\t\t\t-----------------RECORD HAS BEEN SUCCESSFULLY UPDATED---------------")
                                file.commit()
                                break
                            else:
                                print("\t\t\t-----------THIS ID ALREADY EXISTS!!!!!-----------------")
                                print("\t\t\t---------PLEASE TRY AGAIN-------------")
                        elif d==3:
                            m=input("Enter New Name: ")
                            n=int(input("Enter New ID: "))
                            o=int(input("Enter New salary: "))
                            p=input("Enter New Specialization: ")
                            b.execute("update doctor set Name='{}',ID='{}',salary='{}',Specialization='{}' where ID='{}'".format(m,n,o,p,i[1]))
                            print("\t\t\t-----------------RECORD HAS BEEN SUCCESSFULLY UPDATED---------------")
                            file.commit()
                            break
                        else:
                            print("\t\t\t----------INVALID INPUT--------")
        elif choice==2:
            ID=input("Enter ID: ")
            b.execute("select * from doctor where ID='{}'".format(ID))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t----------NO RECORD FOUND!!  -------")
            else:
                for i in data:
                    print(tabulate.tabulate([i],headers=['Name','ID','Salary','Specialization'],tablefmt='pretty'))
                    c=input("Press Y to alter this record: ")
                    if c.upper()=='Y':
                        print("1. Update Name\n2. Update ID\n3. Update All details")
                        d=int(input("Enter choice:"))
                        if d==1:
                            n=input("Enter New Name: ")
                            b.execute("update doctor set Name='{}' where ID='{}'".format(n,i[1]))
                            print("\t\t\t-----------------RECORD HAS BEEN SUCCESSFULLY UPDATED---------------")
                            file.commit()
                            break
                        elif d==2:
                            n=input("Enter New ID: ")
                            b.execute("select * from doctor where ID='{}'".format(n))
                            data1=b.fetchall()
                            if data1==[]:
                                b.execute("update doctor set ID='{}' where ID='{}'".format(n,i[1]))
                                print("\t\t\t-----------------RECORD HAS BEEN SUCCESSFULLY UPDATED---------------")
                                file.commit()
                                break
                            else:
                                print("\t\t\t-----------THIS ID ALREADY EXISTS!!!!!-----------------")
                                print("\t\t\t---------PLEASE TRY AGAIN-------------")
                        elif d==3:
                            m=input("Enter New Name: ")
                            n=int(input("Enter New ID: "))
                            o=int(input("Enter New salary: "))
                            p=input("Enter New Specialization: ")
                            b.execute("update doctor set Name='{}',ID='{}',salary='{}',Specialization='{}' where ID='{}'".format(m,n,o,p,i[1]))
                            print("\t\t\t-----------------RECORD HAS BEEN SUCCESSFULLY UPDATED---------------")
                            file.commit
                            break
                        else:
                            print("\t\t\t----------INVALID INPUT--------")
    elif ch==2:
        print("1. Find record using Patient's name\n2. Find record using Patient's ID")
        choice=int(input("Enter choice: "))
        if choice==1:
            name=input("Enter Name: ")
            b.execute("select * from patient where Name='{}'".format(name))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t----------NO RECORD FOUND!!  -------")
            else:
                for i in data:
                    print(tabulate.tabulate([i],headers=['Name','ID','Disease','Date_Admitted','Address'],tablefmt='pretty'))
                    c=input("Press Y to alter this record: ")
                    if c.upper()=='Y':
                        print("1. Update Name\n2. Update ID\n3. Update All details")
                        d=int(input("Enter choice:"))
                        if d==1:
                            n=input("Enter New Name: ")
                            b.execute("update patient set Name='{}' where ID='{}'".format(n,i[1]))
                            print("\t\t\t-----------------RECORD HAS BEEN SUCCESSFULLY UPDATED---------------")
                            file.commit()
                            break
                        elif d==2:
                            n=input("Enter New ID: ")
                            b.execute("select * from patient where ID='{}'".format(n))
                            data1=b.fetchall()
                            if data1==[]:
                                b.execute("update patient set ID='{}' where ID='{}'".format(n,i[1]))
                                print("\t\t\t-----------------RECORD HAS BEEN SUCCESSFULLY UPDATED---------------")
                                file.commit()
                                break
                            else:
                                print("\t\t\t-----------THIS ID ALREADY EXISTS!!!!!-----------------")
                                print("\t\t\t---------PLEASE TRY AGAIN-------------")
                        elif d==3:
                            m=input("Enter New Name: ")
                            n=int(input("Enter New ID: "))
                            o=input("Enter Disease: ")
                            p=input("Enter New Date_of_admission: ")
                            q=input("Enter New Address: ")
                            b.execute("update patient set Name='{}',ID='{}',Disease='{}',Date_Admitted='{}',Address='{}' where ID='{}'".format(m,n,o,p,q,i[1]))
                            print("\t\t\t-----------------RECORD HAS BEEN SUCCESSFULLY UPDATED---------------")
                            file.commit()
                            break
                        else:
                            print("\t\t\t----------INVALID INPUT--------")
        elif choice==2:
            ID=input("Enter ID: ")
            b.execute("select * from patient where ID='{}'".format(ID))
            data=b.fetchall()
            if data==[]:
                print("\t\t----------NO RECORD FOUND!!  -------")
            else:
                for i in data:
                    print(tabulate.tabulate([i],headers=['Name','ID','Disease','Date_Admitted','Address'],tablefmt='pretty'))
                    c=input("Press Y to alter this record: ")
                    if c.upper()=='Y':
                        print("1. Update Name\n2. Update ID\n3. Update All details")
                        d=int(input("Enter choice:"))
                        if d==1:
                            n=input("Enter New Name: ")
                            b.execute("update patient set Name='{}' where ID='{}'".format(n,i[1]))
                            print("\t\t\t-----------------RECORD HAS BEEN SUCCESSFULLY UPDATED---------------")
                            file.commit()
                            break
                        elif d==2:
                            n=input("Enter New ID: ")
                            b.execute("select * from patient where ID='{}'".format(n))
                            data1=b.fetchall()
                            if data1==[]:
                                b.execute("update patient set ID='{}' where ID='{}'".format(n,i[1]))
                                print("\t\t\t-----------------RECORD HAS BEEN SUCCESSFULLY UPDATED---------------")
                                file.commit()
                                break
                            else:
                                print("\t\t\t-----------THIS ID ALREADY EXISTS!!!!!-----------------")
                                print("\t\t\t---------PLEASE TRY AGAIN-------------")
                        elif d==3:
                            m=input("Enter New Name: ")
                            n=int(input("Enter New ID: "))
                            o=input("Enter Disease: ")
                            p=input("Enter New Date_of_admission: ")
                            q=input("Enter New Address: ")
                            b.execute("update patient set Name='{}',ID='{}',Disease='{}',Date_Admitted='{}',Address='{}' where ID='{}'".format(m,n,o,p,q,i[1]))
                            print("\t\t\t-----------------RECORD HAS BEEN SUCCESSFULLY UPDATED---------------")
                            file.commit()
                            break
                        else:
                            print("\t\t----------INVALID INPUT--------")
        else:
            print("\t\t----------INVALID INPUT--------")
    else:
        print("\t\t----------INVALID CHOICE--------")    
def restore_record():
    print("1. Restore Doctor Records\n2. Restore Patient Records")
    ch=int(input("Enter Choice: "))
    if ch==1:
        print("1. Restore Using Name\n2. Restore using ID")
        choice=int(input("Enter Choice: "))
        if choice==1:
            name=input("Enter Name: ")
            b.execute("select * from restore_doctor where name='{}'".format(name))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t----------NO SUCH RECORD DELETED---------")
            else:
                for i in data:
                    print(tabulate.tabulate([i],headers=['Name','ID','Salary','Specialization'],tablefmt='pretty'))
                    x=input("ENTER Y to  restore this data: ")
                    if x.upper()=='Y':
                        b.execute("insert into doctor values('{}','{}','{}','{}')".format(i[0],i[1],i[2],i[3]))
                        b.execute("delete from restore_doctor where ID='{}'".format(i[1]))
                        file.commit()
                        print("\t\t\t-----------THIS RECORD IS SUCCESSFULLY RESTORED---------")
                        break
        elif choice==2:
            ID=int(input("Enter ID: "))
            b.execute("select * from restore_doctor where ID='{}'".format(ID))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t----------NO SUCH RECORD DELETED---------")
            else:
                print(tabulate.tabulate(data,headers=['Name','ID','Salary','Specialization'],tablefmt='pretty'))
                x=input("ENTER Y to  restore this data: ")
                if x.upper()=='Y':
                    b.execute("insert into doctor values('{}','{}','{}','{}')".format(data[0][0],data[0][1],data[0][2],data[0][3]))
                    b.execute("delete from restore_doctor where ID='{}'".format(ID))
                    file.commit()
                    print("\t\t\t-----------THIS RECORD IS SUCCESSFULLY RESTORED---------")
        else:
            print("\t\t\t-----------INVALID INPUT--------------")
    elif ch==2:
        print("1. Restore Using Name\n2. Restore using ID")
        choice=int(input("Enter Choice: "))
        if choice==1:
            name=input("Enter Name: ")
            b.execute("select * from restore_patient where name='{}'".format(name))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t----------NO SUCH RECORD DELETED---------")
            else:
                for i in data:
                    print(tabulate.tabulate([i],headers=['Name','ID','Disease','Date_Admitted','Address'],tablefmt='pretty'))
                    x=input("ENTER Y to  restore this data: ")
                    if x.upper()=='Y':
                        b.execute("insert into patient values('{}','{}','{}','{}','{}')".format(i[0],i[1],i[2],i[3],i[4]))
                        b.execute("delete from restore_patient where ID='{}'".format(i[1]))
                        file.commit()
                        print("\t\t\t-----------THIS RECORD IS SUCCESSFULLY RESTORED---------")
                        break
        elif choice==2:
            ID=int(input("Enter ID: "))
            b.execute("select * from restore_patient where ID='{}'".format(ID))
            data=b.fetchall()
            if data==[]:
                print("\t\t\t----------NO SUCH RECORD DELETED---------")
            else:
                print(tabulate.tabulate(data,headers=['Name','ID','Disease','Date_Admitted','Address'],tablefmt='pretty'))
                x=input("ENTER Y to  restore this data: ")
                if x.upper()=='Y':
                    b.execute("insert into patient values('{}','{}','{}','{}','{}')".format(data[0][0],data[0][1],data[0][2],data[0][3],data[0][4]))
                    b.execute("delete from restore_patient where ID='{}'".format(ID))
                    file.commit()
                    print("\t\t\t-----------THIS RECORD IS SUCCESSFULLY RESTORED---------")
        else:
            print("\t\t\t-----------INVALID INPUT--------------")
    else:
        print("\t\t\t-------------INVALID CHOICE----------")
                
def export_record():
    print("1. Export Doctor Details\n2. Export Patient Details")
    import csv
    ch=int(input("Enter Choice: "))
    if ch==1:
        x=input("Enter Name of file: ")
        y='C:\\Users\\LAKSHAY\\OneDrive\\Desktop\\PYTHON Programs\\Usersfiles\\'+x+'.csv'
        try:
            f=open(y)
            print("\t\t\t----------THIS FILE NAME IS ALREADY PRESENT!!-------------")
            print("\t\t\t-------------------PLEASE TRY AGAIN!!---------------")
        except:
            f=open(y,'w',newline='')
            b.execute("select * from Doctor")
            data=b.fetchall()
            data1=csv.writer(f)
            data1.writerows(data)
            print("Your file Has been Created at location: ",y)
            f.close()
    elif ch==2:
        x=input("Enter Name of file: ")
        y='C:\\Users\\LAKSHAY\\OneDrive\\Desktop\\PYTHON Programs\\Usersfiles\\'+x+'.csv'
        try:
            f=open(y)
            print("\t\t\t----------THIS FILE NAME IS ALREADY PRESENT!!-------------")
            print("\t\t\t-------------------PLEASE TRY AGAIN!!---------------")
        except:
            f=open(y,'w',newline='')
            b.execute("select * from Patient")
            data=b.fetchall()
            data1=csv.writer(f)
            data1.writerows(data)
            print("Your file Has been Created at location: ",y)
            f.close()
    else:
        print("\t\t\t-------------INVALID INPUT!!!!------------------")
def view_record():
    print("1. View Doctor's Records\n2. View Patient Records")
    ch=int(input("Enter Choice: "))
    if ch==1:
        print("1. View All Records\n2. View Records in Alphabetical order")
        print("3. View Records in Increasing Doctor ID")
        print("4. View Records in Decreasing Doctor ID")
        choice=int(input("Enter choice: "))
        if choice==1:
            b.execute("select * from doctor")
            data=b.fetchall()
            if data==[]:
                print("\t\t----------NO RECORD FOUND!!  -------")
            else:
                print("\t\t------------DOCTOR Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Salary','Specialization'],tablefmt='pretty'))
        elif choice==2:
            b.execute("select * from doctor order by Name")
            data=b.fetchall()
            if data==[]:
                print("\t\t----------NO RECORD FOUND!!-------")
            else:
                print("\t\t------------DOCTOR Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Salary','Specialization'],tablefmt='pretty'))
        elif choice==3:
            b.execute("select * from doctor order by ID")
            data=b.fetchall()
            if data==[]:
                print("\t\t----------NO RECORD FOUND!!  -------")
            else:
                print("\t\t------------DOCTOR Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Salary','Specialization'],tablefmt='pretty'))
        elif choice==4:
            b.execute("select * from doctor order by ID desc")
            data=b.fetchall()
            if data==[]:
                print("\t\t----------NO RECORD FOUND!!  -------")
            else:
                print("\t\t------------DOCTOR Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Salary','Specialization'],tablefmt='pretty'))
        else:
            print("\t\t----------INVALID INPUT!!--------")
    elif ch==2:
        print("1. View All Records\n2. View Records in Alphabetical order")
        print("3. View Records in Increasing Patient ID")
        print("4. View Records in Decreasing Patient ID")
        choice=int(input("Enter choice: "))
        if choice==1:
            b.execute("select * from patient")
            data=b.fetchall()
            if data==[]:
                print("\t\t----------NO RECORD FOUND!!  -------")
            else:
                print("\t\t------------PATIENT Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Disease','Date_Admitted','Address'],tablefmt='pretty'))
        elif choice==2:
            b.execute("select * from patient order by Name")
            data=b.fetchall()
            if data==[]:
                print("\t\t----------NO RECORD FOUND!!-------")
            else:
                print("\t\t------------PATIENT Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Disease','Date_Admitted','Address'],tablefmt='pretty'))
        elif choice==3:
            b.execute("select * from patient order by ID")
            data=b.fetchall()
            if data==[]:
                print("\t\t----------NO RECORD FOUND!!  -------")
            else:
                print("\t\t------------PATIENT Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Disease','Date_Admitted','Address'],tablefmt='pretty'))
        elif choice==4:
            b.execute("select * from patient order by ID desc")
            data=b.fetchall()
            if data==[]:
                print("\t\t----------NO RECORD FOUND!!  -------")
            else:
                print("\t\t------------PATIENT Records-------")
                print(tabulate.tabulate(data,headers=['Name','ID','Disease','Date_Admitted','Address'],tablefmt='pretty'))
        else:
            print("\t\t----------INVALID INPUT!!--------")
    else:
        print("\t\t----------INVALID INPUT!!--------")
