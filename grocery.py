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
    print("list cannot be empty.")
else:
    while True:
        print(Fore.GREEN+"="*20,"Grocery Store Inventory System","="*20+Style.RESET_ALL)
        print(Fore.YELLOW+"1.Add new grocery item"+Style.RESET_ALL)  
        print(Fore.YELLOW+"2.Display all items"+Style.RESET_ALL)
        print(Fore.YELLOW+"3.Search item by name"+Style.RESET_ALL)
        print(Fore.YELLOW+"4.Update item quantity"+Style.RESET_ALL) 
        print(Fore.YELLOW+"5.Delete item"+Style.RESET_ALL)
        print(Fore.YELLOW+"6.Exit"+Style.RESET_ALL)
        ch=int(input("Enter your choice = "))
        #add items
        if ch==1:
            #add id
            id=input("Enter the Id = ")
            if id=="":
                print("ID may be required.")
                continue
            if not id.isdigit():
                print("Only digit allowed.")
                continue
            id=int(id)
        #add name
            name=input("Enter a item name = ")
            if name =="":
                print("Name may be required.")
                continue
            if not name.isalpha():
                print("Only alphabets allowed.")
                continue
        #add Quantity
            quantity=input("Enter the quantity of items : ")
            if quantity =="":
                print("Quantity cannot be empty")
                continue
            if not quantity.isdigit():
                print("Only digit allowed.")
                continue
            quantity=int(quantity)
            if not quantity > 0:
                print("Quantity always startwith one")
                continue
        #add price
            price=input("Enter price of item :")
            if price =="":
                print("price cannot be empty.")
                continue
            if not price.isdigit():
                print("Only digit allowed.")
                continue
            price=int(price)
            grocery.append([id,name,quantity,price])
            print("Items added successfully.")
        #displya items    
        if ch==2:
            if not grocery:
                print("Items not found")
            else:
                print("-"*50) 
                print(f"{'ID':<10}{'Name':<15}  {'Quantity':<10}   {'Price':<5}")
                print("-"*50)  
                for i in grocery:
                     print(f"{i[0]:<10} {i[1]:<15}  {i[2]:<10}   {i[3]:<5}")
                print("-"*50)  
        #search item by name
        if ch==3:
            found=False
            i_name=input("Enter name of item = ")
            for ch in grocery:
                if ch[1]== i_name:
                    print("-"*50) 
                    print(f"{'ID':<10}{'Name':<15}  {'Quantity':<10}   {'Price':<5}")
                    print("-"*50)  
                    print(f"{ch[0]:<10} {ch[1]:<15}  {ch[2]:<10}   {ch[3]:<5}")
                    print("-"*50) 
                    break
                if not found:
                    print("Item not found.")  
        if ch==4:
                             
            break


