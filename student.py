'''
student management system

1.Add the student
2.Display all student
3.Search student by roll number
4.update the record
5.Delete student record
6.exit
'''
from colorama import Fore,Back,Style,init
init()
student=[]
if student == "":
    print("list cannot be empty")
else:
    while True:
        print("1.Add the student record.")
        print("2.Display all student")
        print("3.Search student by roll number")
        print("4.Update student marks")
        ch=int(input(Fore.LIGHTYELLOW_EX+"enter your choice = "+Style.RESET_ALL))
        match ch:
            case 1:
                #take student id
                id=input(Fore.LIGHTMAGENTA_EX+"enter student id = "+Style.RESET_ALL).strip()
                if id=="":
                    print(Fore.RED+"id cannot be empty"+Style.RESET_ALL)
                    continue
                # check digit
                if not id.isdigit():
                    print(Fore.RED+"it only allowed digit"+Style.RESET_ALL)
                    continue
                #check dublicate id
                found=False
                for i in student:
                    if i[0]==id:
                        found=True
                        break
                if found:
                    print(Fore.RED+"id is already exit"+Style.RESET_ALL)
                    continue
                id=int(id)

                # take student name
                name=input(Fore.LIGHTMAGENTA_EX+"enter student name = "+Style.RESET_ALL).strip().lower()
                if name == "":
                    print(Fore.RED+"name cannot be empty"+Style.RESET_ALL)
                    continue
                # check the albhabets
                if not name.replace(" ","").isalpha():
                    print(Fore.RED+"only allowed the albhabets"+Style.RESET_ALL)
                    continue
                #take student mobile number
                mob=input(Fore.LIGHTMAGENTA_EX+"enter student mobile number = "+Style.RESET_ALL).strip()
                if mob =="":
                    print(Fore.RED+"mobile number cannot be empty"+Style.RESET_ALL)
                    continue
                #check the number of digit in mobile number
                if len(mob) != 10:
                    print(Fore.RED+"it allowed only 10 digit"+Style.RESET_ALL)
                    continue
                #check the valid and indian number
                if not mob.startswith("9") and not mob.startswith("8") and not mob.startswith("7") and not mob.startswith("6"):
                    print(Fore.RED+"invalid number...please enter a valid number"+Style.RESET_ALL)
                    continue
                if not mob.isdigit():
                    print(Fore.RED+"it's only  allowed digit"+Style.RESET_ALL)
                    continue
                mob=int(mob)
                # take student marks
                marks=input(Fore.LIGHTMAGENTA_EX+"enter student marks = "+Style.RESET_ALL).strip()
                if marks=="":
                    print(Fore.RED+"marks cannot be empty"+Style.RESET_ALL)
                    continue
                #check the digit of marks
                if not marks.isdigit():
                    print(Fore.RED+"marks only allowed the digit"+Style.RESET_ALL)
                    continue
                marks=int(marks) 
                #check the length of marks
                if marks < 0 or marks > 100:
                    print(Fore.RED+" marks only allowed the 1 to 100"+Style.RESET_ALL)
                    continue 
                #take student city
                city=input(Fore.LIGHTMAGENTA_EX+"enter a student city = "+Style.RESET_ALL).strip().lower()
                if city =="":
                    print(Fore.RED+"city cannot be empty"+Style.RESET_ALL)
                    continue
                if not city.isalpha():
                    print(Fore.RED+"city only allowed alphabets"+Style.RESET_ALL)
                    continue 
                student.append([id,name,mob,marks,city])  
                print(Fore.GREEN+"student record add successfully!"+Style.RESET_ALL)               
            case 2:
                #display all student
                print(Fore.YELLOW+"-"*60+Style.RESET_ALL)
                print(Fore.LIGHTMAGENTA_EX+f"{'ID':<10}{'Name':<15}  {'Mobile No':<10}   {'Marks':<4}   {'City':<10}"+Style.RESET_ALL)
                print(Fore.YELLOW+"-"*60+Style.RESET_ALL)
                for i in student:
                     print(Fore.LIGHTYELLOW_EX+f"{i[0]:<10}{i[1]:<15}  {i[2]:<10}   {i[3]:<4}   {i[4]:<10}"+Style.RESET_ALL)
                print(Fore.YELLOW+"-"*60+Style.RESET_ALL)     
            case 3:
                #Search student by roll number
                found=False
                sid=int(input("Enter a id for student = "))
                for i in student:
                    if i[0]==sid:
                        found=True
                        print(Fore.YELLOW+"-"*60+Style.RESET_ALL)
                        print(Fore.LIGHTMAGENTA_EX+f"{'ID':<10}{'Name':<15}  {'Mobile No':<10}   {'Marks':<4}   {'City':<10}"+Style.RESET_ALL)
                        print(Fore.YELLOW+"-"*60+Style.RESET_ALL)
                        print(Fore.LIGHTYELLOW_EX+f"{i[0]:<10}{i[1]:<15}  {i[2]:<10}   {i[3]:<4}   {i[4]:<10}"+Style.RESET_ALL)
                        print(Fore.YELLOW+"-"*60+Style.RESET_ALL) 
                        break
                if not found:
                    print(Fore.RED+f"student record not found."+Style.RESET_ALL)
            case 4:
                #Update student marks 
                found=False
                sid=int(input("Enter a ID for student = "))
                for i in student:
                    if i[0]==sid:
                        #add_marks=int(input("Enter a updating marks :"))
                        #i[3]=add_marks
                        found=True
                        print(Fore.LIGHTMAGENTA_EX+"1. update name"+Style.RESET_ALL)
                        print(Fore.LIGHTMAGENTA_EX+"2. update mobile no"+Style.RESET_ALL)
                        print(Fore.LIGHTMAGENTA_EX+"3. update marks"+Style.RESET_ALL)
                        print(Fore.LIGHTMAGENTA_EX+"4. update city"+Style.RESET_ALL)
                        ch=int(input(Fore.LIGHTBLUE_EX+"Enter a updating choice :"+Style.RESET_ALL))
                        match ch:
                            case 1:
                                i[1]=input(Fore.CYAN+"Enter a new name :"+Style.RESET_ALL)
                                print(Fore.GREEN+"Name is updated successfully"+Style.RESET_ALL)
                                continue
                            case 2:
                                i[2]=int(input(Fore.CYAN+"Enter new mobile no :"+Style.RESET_ALL))
                                print(Fore.GREEN+"Mobile no updated sucessfuly"+Style.RESET_ALL)
                                continue
                            case 3:
                                i[3]=int(input(Fore.CYAN+"Enter new marks :"+Style.RESET_ALL))
                                print(Fore.GREEN+"Marks upadted successfully"+Style.RESET_ALL)
                                continue
                            case 4:
                                i[4]=input(Fore.CYAN+"Enter a new city :"+Style.RESET_ALL)
                                print(Fore.GREEN+"City is updated successfully"+Style.RESET_ALL)
                                continue
                            case _:
                                print(Fore.RED+"Invalid choice"+Style.RESET_ALL)            
                        break
                if not found:
                    print(Fore.RED+"Student Record not found."+Style.RESET_ALL) 
                    
            case 5:
                #delete the student record
                found=False
                sid=int(input("Enter a ID for student = "))
                for i in student:
                    if i[0]==sid:
                        student.remove(i)
                        found=True
                        print(Fore.GREEN+"Record delete successfully"+Style.RESET_ALL)
                        break
                if not found:
                    print(Fore.RED+"Student Record not found."+Style.RESET_ALL)   
            case 6:
                print("Exit")
                break             
            case _:
                print("invalid choice")
                break        