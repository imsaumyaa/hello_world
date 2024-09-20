#printing diamond

a = input("enter size of diamond(row no.)")
a = int(a)

for i in range(a):
  print(" " * (a-i), "x" * (2*i+1))
  
for i in range(a-2 , -1 , -1):
  print(" " * (n-i), "*" (2*i+1))
  
