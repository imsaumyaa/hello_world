#divisor calculator
#user input
a = input("enter the no.")
a = int(a)

#make an empty list to store the no.of intrest
divisor = []

#for loop
for i in range(1,a+1):
	if a % i == 0:
		divisor.append(i)
	
#print the result
print(divisor)
