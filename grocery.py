'''
Mini Project : Grocery Store Inventory System
1. Add new grocery item
2. Display all items
3. Search item by name
4. update item quantity
5. Delete item quntity 

- append()
- remove()
- pop()
- index()
- count()
- nested lists

'''
from colorama import Fore,Back,Style,init
init()
grocery=[]
if grocery=="":
    print(Fore.RED+"list cannot be empty."+Style.RESET_ALL)
else:
    while True:
        print(Fore.GREEN+"="*20,"Grocery Store Inventory System","="*20+Style.RESET_ALL)
        print(Fore.YELLOW+"1.Add new grocery item"+Style.RESET_ALL)  
        print(Fore.YELLOW+"2.Display all items"+Style.RESET_ALL)
        print(Fore.YELLOW+"3.Search item by name"+Style.RESET_ALL)
        print(Fore.YELLOW+"4.Update item quantity"+Style.RESET_ALL) 
        print(Fore.YELLOW+"5.Delete item"+Style.RESET_ALL)
        print(Fore.YELLOW+"6.Exit"+Style.RESET_ALL)
        ch=int(input(Fore.GREEN+"Enter your choice = "+Style.RESET_ALL))
        #add items
        if ch==1:
            #add id
            id=input(Fore.LIGHTCYAN_EX+"Enter the Id = "+Style.RESET_ALL)
            if id=="":
                print(Fore.RED+"ID may be required."+Style.RESET_ALL)
                continue
            if not id.isdigit():
                print(Fore.RED+"Only digit allowed."+Style.RESET_ALL)
                continue
            id=int(id)
        #add name
            name=input(Fore.LIGHTCYAN_EX+"Enter a item name = "+Style.RESET_ALL)
            if name =="":
                print(Fore.RED+"Name may be required."+Style.RESET_ALL)
                continue
            if not name.isalpha():
                print(Fore.RED+"Only alphabets allowed."+Style.RESET_ALL)
                continue
        #add Quantity
            quantity=input(Fore.LIGHTCYAN_EX+"Enter the quantity of items : "+Style.RESET_ALL)
            if quantity =="":
                print(Fore.RED+"Quantity cannot be empty"+Style.RESET_ALL)
                continue
            #if not quantity.isalnum():
                #print(Fore.RED+"please enter correct quantity."+Style.RESET_ALL)
                #continue
            if not quantity.isdigit():
                print(Fore.RED+"Only Digit Allowed."+Style.RESET_ALL)  
                continue  
            quantity=int(quantity)
            if not quantity > 0:
                print(Fore.RED+"Quantity always startwith one"+Style.RESET_ALL)
                continue
        #add price
            price=input(Fore.LIGHTCYAN_EX+"Enter price of item :"+Style.RESET_ALL)
            if price =="":
                print(Fore.RED+"price cannot be empty."+Style.RESET_ALL)
                continue
            if not price.isdigit():
                print(Fore.RED+"Only digit allowed."+Style.RESET_ALL)
                continue
            price=int(price)
            grocery.append([id,name,quantity,price])
            print(Fore.GREEN+"Items added successfully."+Style.RESET_ALL)
        #displya items    
        if ch==2:
            if not grocery:
                print(Fore.RED+"Items not found"+Style.RESET_ALL)
            else:
                print(Fore.LIGHTBLUE_EX+"-"*50+Style.RESET_ALL) 
                print(Fore.WHITE+f"{'ID':<10}{'Name':<15}  {'Quantity':<10}   {'Price':<5}"+Style.RESET_ALL)
                print(Fore.LIGHTBLUE_EX+"-"*50+Style.RESET_ALL)  
                for i in grocery:
                     print(Fore.LIGHTYELLOW_EX+f"{i[0]:<10} {i[1]:<15}  {i[2]:<10}   {i[3]:<5}"+Style.RESET_ALL)
                print(Fore.LIGHTBLUE_EX+"-"*50+Style.RESET_ALL)  
        #search item by name
        if ch==3:
            found=False
            i_name=input(Fore.LIGHTCYAN_EX+"Enter name of item = "+Style.RESET_ALL)
            for ch in grocery:
                if ch[1]== i_name:
                    found=True
                    print("-"*50) 
                    print(f"{'ID':<10}{'Name':<15}  {'Quantity':<10}   {'Price':<5}")
                    print("-"*50)  
                    print(f"{ch[0]:<10} {ch[1]:<15}  {ch[2]:<10}   {ch[3]:<5}")
                    print("-"*50) 
                    break
                if not found:
                    print(Fore.RED+"Item not found."+Style.RESET_ALL)  
        if ch==4:
            found=False
            i_name=input(Fore.LIGHTCYAN_EX+"Enter name of item = "+Style.RESET_ALL)
            for ch in grocery:
                if ch[1]== i_name:
                    found=True
                    update_q=int(input(Fore.LIGHTCYAN_EX+"Enter updating quantity = "+Style.RESET_ALL))
                    ch[2]=update_q
                    print(Fore.GREEN+"Item Updated successfully."+Style.RESET_ALL)
                    break
                if not found:
                    print(Fore.RED+"Item not found."+Style.RESET_ALL)
        #Delete the item
        if ch==5:
            found=False
            i_name=input(Fore.LIGHTCYAN_EX+"Enter name of item = "+Style.RESET_ALL)
            for ch in grocery:
                if ch[1]== i_name:
                    found=True
                    grocery.remove(ch)
                    print(Fore.GREEN+"Item Deleted successfully"+Style.RESET_ALL)
                    break
                if not found:
                    print(Fore.RED+"Item not found"+Style.RESET_ALL)
        # Exit
        if ch==6:
            print(Fore.GREEN+"Thank you..visit again"+Style.RESET_ALL)
            break
        if ch==7:
            print(Fore.RED+"Invalid choice"+Style.RESET_ALL)
            break


