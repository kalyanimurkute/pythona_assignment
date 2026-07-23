'''
project 1: Text Analyzer system
1.count total character ,words,sentences
2.count vowels, consonants,digit and special character
3.convert text to uppercase and lowercase
4.check whether a specific word exists in the text 
5.remove the extra space 
'''
from colorama import init, Fore, Back, Style
init()
text=input("enter a sentences = ")
if text == " ":
    print("text cannot be empty")
else:
    while True:
        print("1.count total character ,words,sentences")
        print("2.count vowels, consonants,digit and special character")
        print("3.convert text to uppercase and lowercase")    
        print("4.check whether a specific word exists in the text ")
        print("5.remove the extra space ")
        print("6.exit")
        ch=int(input("enter your choice = "))
        match ch:
            case 1:
               ch=len(text)
               print("Total characters = ",Fore.GREEN ,ch,Style.RESET_ALL)
               word=len(text.split())
               print("Total words = ",Fore.GREEN ,word,Style.RESET_ALL)
               sent=text.count(".")+text.count("!")+text.count("&")
               print("Total sentences = ",Fore.GREEN ,sent,Style.RESET_ALL)
            case 2:
                count=0
                consonant=0
                digit=0
                special=0
                for ch in text.lower():
                    if ch in ('a','e','i','o','u','A'):
                        count +=1
                    else:
                        consonant +=1     
                print("Total vowels = ",Fore.GREEN ,count,Style.RESET_ALL)
                print("Total consonants = ",Fore.GREEN ,consonant,Style.RESET_ALL)
                for ch in text:
                    if ch.isdigit():
                        digit +=1      
                print("Total digit is = ",Fore.GREEN ,digit,Style.RESET_ALL)  
                for ch in text:
                    if ch in ('@','#','%','&','^'):
                        special +=1
                print("Total special character = ",Fore.GREEN ,special,Style.RESET_ALL) 
                break                     
            case 3:
                print(text.upper(),Style.RESET_ALL)
                print(text.lower())
                break
            case 4:
                word=input("enter a words = ")
                if word in text.split():
                    print("Total special character = ",Fore.GREEN ,special,Style.RESET_ALL) 
                    break                     
                else:
                    print(Fore.RED ,f"{word} not found",Style.RESET_ALL)
                break       
            case 5:
                print(text.strip())
                break
            case 6:
                print(Fore.BLUE ,"thank you visit for this project!",Style.RESET_ALL)
                break
            case _:
                print(Fore.RED ,"invalid choice ",Style.RESET_ALL)
           
     