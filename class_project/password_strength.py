'''
project : password strngth checker

1. check minimum password length
2. check presences of uppercase letter
3. check presences of lowercase letter
4. check presences of digit
5. check presences of special character
6. display password strength result
'''

#check the paswword strength
passw=input("enter a password = ")
if passw =="":
    print("password cannot be empty")
else:
    while True:
        print("1.check minimum password length")
        print("2.check presences of uppercase letter")
        print("3.check presences of lowercase letter")
        print("4.check presences of digit") 
        print("5.check presences of special character")
        print("6.display password strength result")   
        print("7.exit")
        ch=int(input("enter your choice = "))
        match ch:
            case 1:
                if 6 <= len(passw) <= 15:
                    print("your password lenght is better")
                else:
                    print("please enter a 6 to 15 digit and characters ")    
            case 2:
                found=False
                for i in passw:
                    if i.isupper():
                        found=True
                        break
                if found :
                    print("upper case letter is present")
                else:
                    print("upper case letter is not present")        
            case 3:
                found = False
                for i in passw:
                    if i.islower():
                        found=True
                        break
                if found:
                    print("lower case is present")
                else:
                    print("lower case is not present")        
            case 4:
                found=False
                for i in passw:
                    if i.isdigit():
                        found=True
                        break
                if found:
                    print("digit is present")
                else:
                    print("digti is not present")        
            case 5:
                found=False
                for i in passw:
                    if i in ('@','*','&','%','$'):
                        found=True
                        break
                if found:
                    print("special character is present")
                else:
                    print("special character is not present")        
            case 6:
                score=0
                if 6 <=len(passw) <=15:
                    score +=1
                    
                for i in passw:
                    if i.isupper():
                        score +=1
                        break
                for i in passw:
                    if i.islower():
                        score +=1
                        break
                for i in passw:
                    if i.isdigit():
                        score +=1
                        break
                for i in passw:
                    if i in ('@','*','&','%','$'):
                        score +=1
                        break
                if score == 5:
                    print("your password strength is strong")
                elif score >= 3:
                    print("your password strength is medium")
                else:
                    print("your password strength is weak")                                                   
            case 7:
                print("thank you! visit for this project")
            case _:
                print("invalid choice")    