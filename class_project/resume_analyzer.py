'''
•	Read resume text 
•	Count keywords like: 
o	Python 
o	Django 
o	REST API 
o	SQL 
o	MySQL 
o	Git 
o	HTML 
o	CSS 
o	JavaScript 
•	Display match percentage 
•	Show missing skills 
•	Suggest improvements
'''
from colorama import Fore, Style, Back,init
init()
resume=input("Enter the resume text: ").lower()
skills=["python","django","rest api","sql","mysql","git","html","css","javascript"]
matched_skills=[]
missing_skills=[]
# check for each skill in the resume
for skill in skills:
    if skill in resume:
        matched_skills.append(skill)
    else:
        missing_skills.append(skill)
# calculate match percentage
match_percentage=(len(matched_skills)/len(skills))*100
print(Fore.CYAN+"\n!------------------------Resume Analysis Result------------------------!\n"+Style.RESET_ALL)
print(Fore.LIGHTGREEN_EX+"Matched Skills :"+Style.RESET_ALL)
for skill in matched_skills:
    print("-",skill)
    
#missing skill
print(Fore.RED+"Missing Skill :"+Style.RESET_ALL)
for skill in missing_skills:
    print("-",skill)
    
#percentages        
print(Fore.GREEN+f"Match Percentage: {match_percentage:.2f}%"+Style.RESET_ALL)
 
#suggestions
print(Fore.GREEN+"suggection :"+Style.RESET_ALL) 
if len(missing_skills)==0:
    print(Fore.GREEN+"your resume required all skills."+Style.RESET_ALL)
else:
    print(Fore.RED+"Add the following skills :"+Style.RESET_ALL)
    for skill in missing_skills:
        print("-",skill)    
          