'''
student management system

1.add the student
2.update the studenat
'''
from colorama import Fore,Back,Style,init
init()
student=[Fore.GREEN+Style.RESET_ALL]
if student == "":
    print("list cannot be empty")
else:
    while True:
        print("1.add the student record.")
        print("2.update the student id")
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
                if not name.isalpha():
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
                pass
            case 3:
                print("thank you visit for system")
            case _:
                print("invalid choice")
                break        