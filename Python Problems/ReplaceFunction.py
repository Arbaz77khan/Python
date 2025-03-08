Letter = '''Hi <Name>
Congratulations!!!
You have been selected for our company
Date : <Date>'''

name = input("Enter your name : ")
date = input("Enter date : ")

Letter = Letter.replace("<Name>", name)
Letter = Letter.replace("<Date>", date)

print(Letter)