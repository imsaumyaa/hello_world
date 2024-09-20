#open file in read and write mode

with open('TXT.txt','r') as file:
	lines = file.readlines()
#print(lines)

#counting the no. of times 'of' occured
#print(lines.count("of"))

print(len(lines))
for i in lines:
	print(i)
lines[2].count("of")
para1 = lines[0].split()
para2 = lines[1].split()
para3 = lines[2].split()
para4 = lines[3].split()
para5 = lines[4].split()
para6 = lines[5].split()
para7 = lines[6].split()
para8 = lines[7].split()
#print(para1)
#print(para1.count("of"))

new = []
for i in range(len(lines)):
	new = new + lines[i].split()
print(len(new))
print(new)
print(new.count("of"))

