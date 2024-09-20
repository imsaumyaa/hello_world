#password generator
import random
lower_letter = "abcdefghijklmnopqrstuvwxyz"
upper_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
symbols = "!@#$%^&*~?<|\/{}[](),."
length = int(input("enter the length of the password"))
if length < 4:
	print("password must be more than 3")
else:
	password = []
	password.append(random.choice(lower_letter))
	password.append(random.choice(upper_letter))
	password.append(random.choice(num))
	password.append(random.choice(symbols))
	remaining_choices = lower_letter + upper_letter + num + symbols
	for i in range(length - 4):
	  password.append(random.choice(remaining_choices))
	random.shuffle(password)
	password = ''.join(password)
	print("your password is :", password)

 

