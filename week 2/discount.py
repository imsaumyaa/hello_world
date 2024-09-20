#Discount calculator
#ask cost 
cost = input("Cost of the item is:")
cost = int(cost)

#calculate discount
discount = cost * 0.1

#print discount
print("You get Rs.", discount,"discount")

#display final price
final_price = cost - discount
print("your final price is :", final_price)

