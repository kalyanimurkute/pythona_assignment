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