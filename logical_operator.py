# using "and" operator
hasHighIncome = True
hasGoodCredit = True

if hasHighIncome and hasGoodCredit:
    print("Eligible for loan")
else:
    print("Sorry!")

# using "or" operator
hasHighIncome = False
hasGoodCredit = True

if hasHighIncome or hasGoodCredit:
    print("Eligible for loan")
else:
    print("Sorry!")

# using "not" operator
hasGoodCredit = True
hasCriminalRecord = True

if hasGoodCredit and not hasCriminalRecord:
    print("Eligible for loan")
else:
    print("Sorry!")
