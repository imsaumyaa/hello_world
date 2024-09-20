#open a file to read it
with open("TXT.txt","r") as file:
	lines = file.readlines()

#print it 
#print(lines)

#bring all words in 1 list
new = []
for i in range(len(lines)):
	new = new + lines[i].split()
print(new)

#count of in it
print(new.count("of"))
