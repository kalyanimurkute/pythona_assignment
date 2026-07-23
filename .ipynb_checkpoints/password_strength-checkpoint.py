'''
project : password strngth checker

1. check minimum password length
2. check presences of uppercase letter
3. check presences of lowercase letter
4. check presences of digit
5. check presences of special character
6. display password strength result
'''


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
                if passw > '6' and passw < '15':
                    for passw in  range('A','Z'):
                        print("your password lenght is better")
                else:
                    print("please enter a 6 to 15 digit and characters ")    
            case 2:
                if len(passw.isupper()):
                    print("your password is better")
                else:
                    print("enter password in to a 1 upper case letter.")   
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                print("thank you! visit for this project")