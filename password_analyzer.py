password=input("Enter a password to analyze:")
print("You entered:",password)
length=len(password)
print("Password length is:",length)
if any(char.isupper() for char in password):
    print("Contains Upper Letter")
else:
    print("No Uppeer Letter")
if any(char.islower() for char in password):
    print("Contains Lower Letter")
else:
    print("No Lower Letter")
if any(char.isdigit() for char in password):
    print("Contains Number")
else:
    print("No Number")

import string
if any(char in string.punctuation for char in password):
    print("Contains Special Characters")
else:
    print("No Special Characters")

score=0
if len(password)>=8:
    score+=1
if any(char.isupper() for char in password):
    score+=1
if any(char.islower() for char in password):
    score+=1
if any(char.isdigit()for char in password):
    score+=1
if any(char in string.punctuation for char in password):
    score+=1

if score ==5:
    print("Strong Password")
elif score >=3:
    print("Medium Password")
else:
    print("Weak Password")   

import string

def analyze_password(password):
    print("\n Analyzing Password:",password)
    length=len(password)
    print("Password length is:",length)
    score=0

    if len(password)>=8:
        score+=1

    if any(char.isupper() for char in password):
        print("Contains Uppercase Letters")
        score+=1
    else:
        print("No Uppercase Letters")

    if any(char.islower() for char in password):
        print("Contains Lowercase Letters")
        score+=1
    else:
        print("No Lowercase Letters")

    if any(char.isdigit()for char in password):
        print("Conatains Numbers")
        score+=1
    else:
        print("No Numbers") 

    if any (char in string.punctuation for char in password):
        print("Contains Special Characters")
        score+=1
    else:
        print("No Special characters") 

    if score==5:
        print("Strong Password")
    elif score>=3:
        print("Medium Password")
    else:
        print("Weak Password")    

while True:
    pw=input("Enter Password To Analyze (or type 'exit'to quit):")
    if pw.lower()=="exit":
        print("Thankyou")
        break
    analyze_password(pw)        




    

