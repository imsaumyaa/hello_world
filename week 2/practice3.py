n = input("enter the number")
n = int(n)
for i in range(1,n+1):
	if i % 3 == 0 and i % 5 == 0:
		print("FIZZBUZZ")
	elif i % 3 == 0: 
		print("FIZZ")
	elif i % 5 == 0:
		print("BUZZ")
	
	else :
		print(i)
	
	
	
	
	
	
