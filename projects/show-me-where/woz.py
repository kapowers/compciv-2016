
from utils.geocoding import geocode

B_X = "\033[1m"
B_Z = "\033[0m"

i_command = input("What do you wanna do? ")
if i_command == "hello":
	usertext = input("How do you identify? ")
	print("Hello", B_X + usertext + B_Z)

elif i_command == 'help':
	print(geocode.__name__)
	print(geocode.__doc__)

elif i_command == 'geocode':
	userlocation = input("Where you at, bruh? ")
	print("Ok...geocoding:", userlocation)
	georesult = geocode(userlocation)
	print(georesult)

else:
	print("Sorry, I don't know how to respond to", i_command)