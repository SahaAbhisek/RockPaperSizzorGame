import random

def gamewin(comp,you):
    #if choices are same then return none to get tie
    if comp==you:
        return None

    # if comp chose rock then conditions    
    elif comp=='r':
        if you=='p':
            return True
        elif you=='s':
            return False

    # if comp chose paper then conditions 
    elif comp=='p':
        if you=='s':
            return True
        elif you=='r':
            return False 

    # if comp chose sizzors then conditions 
    elif comp=='s':
        if you=='r':
            return True
        elif you=='p':
            return False               


#Take computer choice using a random number
print("Comp turn: choose rock(r), paper(p), sizzors(s)")
ranNo=random.randint(1,3)
if ranNo==1:
    comp='r'
elif ranNo==2:
    comp='p'
elif  ranNo==3:
    comp='s'

#Taking player choice from the terminal
you=input("your turn: choose rock(r),paper(p), sizzors(s)\n")

#Calling the game function
a=gamewin(comp,you)

#Printing output resultr

print("comp chose=",comp)
print("You chose=",you)

if a==None:
    print("It's a Tie!")
elif a:
    print("You win!")
else:
    print("You lose!")   

