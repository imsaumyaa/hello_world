n = 5
a = []
for i in range(n):
  l1 = []
  p = 0
  for j in range(i):
    l1.append(j)
  for k in l1:
    p+=1
  a.append(p)
k = 0
for l in a :
  k+=l
print(k)
