'''
Mini Project : Employee Management System

features
1.Add new employee
2.Display all employee
3.Search employee
4.Delete the employee
5.Exit
'''
from colorama import Fore,Back,Style,init
init()
employee=[]
if employee =="":
    print(Fore.RED+"Employee list cannot be empty"+Style.RESET_ALL)
else:
    while True:
        print(Fore.LIGHTYELLOW_EX+"="*10,"Employee Management System","="*10+Style.RESET_ALL)
        print(Fore.GREEN+"1.Add new employee"+Style.RESET_ALL)
        print(Fore.GREEN+"2.Display all employee"+Style.RESET_ALL)
        print(Fore.GREEN+"3.Search employee"+Style.RESET_ALL)
        print(Fore.GREEN+"4.Delete employee"+Style.RESET_ALL)
        print(Fore.GREEN+"5.Exit"+Style.RESET_ALL)
        ch=int(input(Fore.LIGHTYELLOW_EX+"Enter your choice :"+Style.RESET_ALL))
        # Add employee
        if ch ==1:
            limit=int(input(Fore.YELLOW+"Enter how many employee you need to add :"+Style.RESET_ALL))
            for i in range(limit):
                print(Fore.LIGHTYELLOW_EX+"\nEnter the details of employee : "+Style.RESET_ALL,i+1)
                #employee ID
                id=input(Fore.CYAN+"Enter employee id : "+Style.RESET_ALL)
                if id =="":
                    print(Fore.RED+"id cannot be empty :"+Style.RESET_ALL)
                    continue
                if not id.isdigit():
                    print(Fore.RED+"ID Only required digits"+Style.RESET_ALL)
                    continue    
                id=int(id) 
                #employee name
                name=input(Fore.CYAN+"enter employee name : "+Style.RESET_ALL)
                if name==" ":
                    print(Fore.RED+"Name may be required"+Style.RESET_ALL)
                    continue
                if not name.replace(" ","").isalpha():
                    print(Fore.RED+"only alphabet allow"+Style.RESET_ALL)
                    continue 
                #employee department
                dpt=input(Fore.CYAN+"Enter Name Of Employee Department :"+Style.RESET_ALL)
                if dpt=="":
                    print(Fore.RED+"Department Cannot Be Empty."+Style.RESET_ALL)
                    continue
                if not dpt.replace(" ","").isalpha():
                    print(Fore.RED+"Only Alphabets Allowed."+Style.RESET_ALL)
                    continue
                #employee salary
                salary=input(Fore.CYAN+"Enter The Salary : "+Style.RESET_ALL)
                if salary =="":
                    print(Fore.RED+"Salary Cannot Be Empty."+Style.RESET_ALL)
                    continue
                if not salary.isdigit():
                    print(Fore.RED+"Only Allowed Digits"+Style.RESET_ALL)
                    continue
                salary=int(salary)
                #create a tuple 
                t_emp=(id,name,dpt,salary)
                
                #add this tuple inside the list
                
                employee.append(t_emp)
                print(Fore.GREEN+"\nEmployee Added Successfully."+Style.RESET_ALL) 
        #Displya all employee
        if ch==2:
            if not employee:
                print(Fore.RED+"Employee Not Found."+Style.RESET_ALL)
            else:
                print(Fore.GREEN+"\nAll Employee Details"+Style.RESET_ALL)
                for emp in employee:
                    print(Fore.YELLOW+"Employee ID = "+Style.RESET_ALL,emp[0])
                    print(Fore.YELLOW+"Employee Name = "+Style.RESET_ALL,emp[1])
                    print(Fore.YELLOW+"Department = "+Style.RESET_ALL,emp[2]) 
                    print(Fore.YELLOW+"Salary = "+Style.RESET_ALL,emp[3])
        #Display the specific employee based on id 
        if ch==3:
            found=False
            eid=int(input(Fore.GREEN+"Enter The Employee ID : "+Style.RESET_ALL))
            for i in employee:
                if i[0]==eid:
                    print(Fore.YELLOW+"\nEmployee Found\n"+Style.RESET_ALL)
                    print(Fore.YELLOW+"Employee ID = "+Style.RESET_ALL,emp[0])
                    print(Fore.YELLOW+"Employee Name = "+Style.RESET_ALL,emp[1])
                    print(Fore.YELLOW+"Department = "+Style.RESET_ALL,emp[2]) 
                    print(Fore.YELLOW+"Salary = "+Style.RESET_ALL,emp[3])
                    found=True
                    break
            if not found:
                print(Fore.RED+"Employee Not Found"+Style.RESET_ALL)  
        #Delete the Employee
        if ch==4:
            found=False
            eid=int(input(Fore.GREEN+"Enter The Employee Id : "+Style.RESET_ALL))
            for i in employee:
                if i[0]==eid:
                    employee.remove(i)
                    found=True
                    print(Fore.GREEN+"Record Delete Successfully."+Style.RESET_ALL)
                    break
            if not found:
                print(Fore.RED+"Employee Record Not Found."+Style.RESET_ALL)    
        #Exit
        elif ch==5:
            print(Fore.GREEN+"\nThank you ...visit again"+Style.RESET_ALL)
            break
        elif ch==6:
            print(Fore.RED+"Invalid Choice"+Style.RESET_ALL)
