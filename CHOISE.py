#MAIN PAGE 

import LOGIN
import newhotel
from os import system
from time import sleep
#for clear the screen
def clear():
	_=system('clear')

#prgm start from here
print('1. Sign In')
print('')
print('2. Login')
print("")

# a loop is created for avoid invalid entry 

loop=1
cut=1

while cut==loop:
	choise=int(input("Please enter ur choise :"))
	if choise == 1:
		break
	elif choise == 2:
		break
	else :
		print(" ""\nInvalid entry\n")
		sleep(2)		
#loop ends here

#clearing the screen
clear()

#from here the control is navagiated to signup or login page

#choise for signup

if choise==1:
	print("")
	print("SIGN_UP PAGE")
	LOGIN.signin()
	clear()
	newhotel.newhotel()
	
#choise for login	

if choise==2:
	 print("")
	 print("LOGIN_PAGE")
	 clear()
	 print("this page is under constration please connect later")
