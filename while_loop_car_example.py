isCarStarted = False
while True:
    command = input(">").lower()

    if command == "help":
        print("""start - to start the car
stop - to stop the car
quit - to exit
""")
    elif command == "start":
        if isCarStarted:
            print("Car already started!")
        else:
            isCarStarted = True
            print("Car started...Ready to go!")
    elif command == "stop":
        if not isCarStarted:
            print("Car already stopped man!!")
        else:
            isCarStarted = False
            print("Car stopped.")
    elif command == "quit":
        break
    else:
        print("I don't understand that...")
