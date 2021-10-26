print ("The price of apple is: ")
apple =int(input())
print ("How many apples doyou want to buy? ")
order =int(input())
amount = apple*order
print ("Your money here: ")
money = int(input())
print(f"The total amount is",amount)
total = money-amount
print (f"You can buy {order} and your change is {total} pesos. ")