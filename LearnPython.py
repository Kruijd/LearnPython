# Enter the Settings and go to Keymap.
# Search for Execute Selection in Console and reassign it to a new shortcut, like Crl+Enter.
# This is the same shortcut to the same action in Spyder and R-Studio.
# Shift+ALT+E
# Created 17-2-2019


numberstaken =[2,5,12,13,17]
print("Hey")

for n in range(1,20):
    if n in numberstaken:
        continue
    print(n)

help(round)

#Function tutorial 15,16

def beef(btc, a=True):
    print("Hoi")
    Amount=btc*12345
    print(Amount)
    if a is True:
        print("True")
    else:
        print("Hoi Jan")
    return Amount


a= beef(1323)


type(a)
print(round(beef(1323, False)/123443,3))



n=range(0,100,5)
b=n[4]

#Flexible amount of arguments; tutorial 17
def add_numbers(*args):
    total=0
    for a in args:
        total +=a
        print(total)

add_numbers(3,5,4,6,8,4,2)

#18 - Unpacking Arguments

#19 Sets

groceries = { "serial","milk","duct tape","beer", "milk"} # milk is er twee maal
print(groceries)

#Dictionaries; keys and values
classmates ={"Tony":"cool but smells", "Emma": "Sits behind me", "Lucy":"Asks too many questions"}
print(classmates)
print(classmates["Emma"])

for k,v in classmates.items():
    print(k+" "+v)

#
