#password generator
import random
import string
#lower_letter = "abcdefghijklmnopqrstuvwxyz"
#upper_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#num = "0123456789"
#symbols = "!@#$%^&*~?<|\/{}[](),."
length = int(input("enter the length of the password"))
if length < 4:
	print("password must be more than 3")
else:
	password = []
	password.append(random.choice(string.ascii_lowercase))
	password.append(random.choice(string.ascii_uppercase))
	password.append(random.choice(string.digits))
	password.append(random.choice(string.punctuation))
	remaining_choices = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
	for i in range(length - 4):
	  password.append(random.choice(remaining_choices))
	random.shuffle(password)
	password = ''.join(password)
	print("your password is :", password)

 

