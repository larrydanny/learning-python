isHot = False
isCold = True

if isHot:
    print("It's a hot day")
    print("Drink plenty of water")
elif isCold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")


# price of a house is $1M
# if buyer has "Good Credit",
# they need to put down "10%"
# otherwise
# they need to put down "20%"
# Print the down payment
housePrice = 1000000  # 1M
hasGoodCredit = True
if hasGoodCredit:
    downPayment = housePrice * 0.1
    print("Down payment is ", downPayment)
else:
    downPayment = housePrice * 0.2
    print("Down payment is ", downPayment)
