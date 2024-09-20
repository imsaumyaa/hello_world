#display no. divisible by 5 from a list

#initialization of the given list to access that list
#make a new empty list to store the value of no. divisible by 5
#running a for loop 
#check divisibility criteria of 5
#print the result


num = [13,23,34,45,56,67,78,89,98,87,76,65,54,43,32,21]
divisibility_check = []
for numbers in num:
	if numbers % 5 == 0:
		divisibility_check.append(numbers)
print("the numbers divisible by 5:", divisibility_check)
