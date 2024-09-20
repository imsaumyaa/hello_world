#arithmetic progression
#8,11,14,17,20,......8+(n-1)*3   f+(n-1)*d (general term)
#sum of N term = (n/2) * (2*f+(n-1)*d)
# user input = f,d,n
#output = nth term and their sum

f = input("enter the first term")
d = input("enter the common difference")
n = input("enter the number of terms")

f = int(f)
d = int(d)
n = int(n)

nth=f+(n-1)*d
ap_sum = (n/2) * (2*f+(n-1)*d)

print("nth term = ",nth)
print("sum upto nth term =",ap_sum)

ap_list = []
for i in range(1,n+1):
	ap_list.append(f+(i-1)*d)
print(ap_list)
	








