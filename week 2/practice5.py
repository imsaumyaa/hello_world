# pallindrome and symmetry
# take input
string = input("enter the string:")

# calculate the length of string
length = len(string)

# initialize a flag if the string is symmetric
is_symmetric = True

# initialize a flag if the string is pallindromic
is_pallindromic = True

# loop through string to check symmetry# loop through string to check pallindrome

mid = length // 2

for i in range(mid):
	
	if string[i] != string[mid + i]:
		is_symmetric = False
	if string[i] != string[length - 1 -i]:
                is_pallindromic = False
                
# print the result
print("The given input is symmetric:", is_symmetric)
print("The given input is pallindromic:", is_pallindromic)

is_symmetric = False
is_pallindromic = False

reverse = string[::-1]
if string == reverse:
	is_pallindromic = True
first_half = string[:mid]
second_half = string[mid:]
if first_half == second_half:
	is_symmetric = True
print("result from list slicing")	
print("The given input is symmetric:", is_symmetric)
print("The given input is pallindromic:", is_pallindromic)

