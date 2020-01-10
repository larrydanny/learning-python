i = 1

while i <= 5:
    print(i)
    i += 1
print("Done")

# *
# **
# ***
# ****
# *****
i = 1

while i <= 5:
    print("*" * i)
    i += 1
print("Done")

# Guessing Game
secretNumber = 6
guessCount = 0
guessLimit = 3
while guessCount < guessLimit:
    guess = int(input("Guess: "))
    guessCount += 1
    if guess == secretNumber:
        print("you win")
        break
else:
    print("Sorry you failed!")
