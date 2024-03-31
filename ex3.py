def order_cost(kilos):
    price = 3*kilos
    if price > 50:
        postage = 4.99
    else:
        postage = 3.49
    return (price+postage)

################

kilos = float(input("Enter the weight of your order of bananas in kilos: "))
print("This order will cost £" + str(order_cost(kilos)) + ", including shipping")
