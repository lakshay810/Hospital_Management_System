#HOSPITAL MANAGEMENT SYSTEM

# Note that to Run this file, you must download the Functions.py file in your device
from functions import *
while True:
    print("\t\t\t\t-----------------HOSPITAL MANAGEMENT SYSTEM-------------------\n\n")
    print("1. Add Record\n2. Search Record\n3. Delete Record\n4. Update Record\n5. Restore Record")
    print("6. Export Record to an Excel File\n7. View Records\n8. EXIT")
    choice=int(input("Enter Choice: "))
    if choice==1:
        add_record()
    elif choice==2:
        search_record()
    elif choice==3:
        delete_record()
    elif choice==4:
        update_record()
    elif choice==5:
        restore_record()
    elif choice==6:
        export_record()
    elif choice==7:
        view_record()
    elif choice==8:
        break
    else:
        print("\t\t-----------------INVALID INPUT---------------")
