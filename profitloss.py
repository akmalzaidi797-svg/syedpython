cost_price = int(input("Enter a cost price"))
selling_price = int(input("Enter a selling price"))

if cost_price < selling_price:
    profit = selling_price - cost_price
    print("We Have Made Profit Of : " , profit)
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("We have Incurred Loss Of : " , loss)
else:
    print("We have made no profit or no loss")
 