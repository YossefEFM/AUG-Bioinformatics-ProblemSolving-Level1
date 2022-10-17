# try it"Traffic light"
x= input ("please enter the signal (G or R or Y)")
if (x== 'G'):
    print ("move it's green")
elif (x== 'R'):
    print ("stop it's red ")
elif (x== 'Y'):
    y = input ("please enter the signal (G or R )")
    if (y== 'G'):
        print("get redy to move")
    elif (y == 'R'):
        print("get ready to stop")
    else :
        print("invalid value")
else :
    print("invalid value")
#//////////////////////////////////////////////////////////////////////////////

# second  "roll the dice"
import random
num = random.randint(1,6)
choise= int (input ("enter your choise from 1 to 6"))
while (num != choise ):
    choise = int(input("another "))
print ("yaaaaay you did it ")
#//////////////////////////////////////////////////////////////////////////////


#welcome function
def welcome (name):
    print ("welcome "+ name)


l = input("enter your name")
welcome (l)