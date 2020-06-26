from os import system
from time import sleep 

def clear():
	_=system('clear')
	
def newhotel():
	global hotelname,t_rooms,ac_rooms,non_ac_rooms,ac_rate,a
	a="hai"
	hotelname=input(" enter ur hotel name : ")
	t_rooms=int(input(" enter total numbers of rooms : "))
	ac_rooms=int(input(" number of ac rooms : "))
	non_ac_rooms=t_rooms-ac_rooms
	ac_rate=int(input(" enter the rate for ac room : "))
	if t_rooms != ac_rooms:
		non_ac_rate=int(input(" enter the rate for non ac room : "))
	#print(ac_rooms,non_ac_rooms)

	
	

