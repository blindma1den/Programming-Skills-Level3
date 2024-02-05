
d1 = ("California (Los Angeles)")
d2 = ("Florida (Miami)")
d3 = ("Texas (Houston)")
d4 = ("Illinois (Chicago)")
d5 = ("Washington (Seattle)")
d6 = ("Massachusetts (Boston)")
d7 = ("Colorado (Denver)")
d8 = ("Georgia (Atlanta)")
d9 = ("Arizona (Phoenix)")
d10 = ("Nevada (Las Vegas)")

def edt(distance):
    if distance < 1000:
        print("Estimated delivery time: 1 day") 
    elif 1000 <= distance < 2000:
        print("Estimated delivery time: 2 day")
    elif 2000 <= distance < 3000:
        print("Estimated delivery time: 3 day")
    elif 3000 <= distance < 4000:
        print("Estimated delivery time: 4 day")
    elif distance > 4000:
        print("Estimated delivery time: 5 day or more")
while True:

    print("Welcome Amazon New York")

    print("How many packages are to be transported?")
    npackages = int(input("Enter a number: "))
    if 0 <= npackages <= 99 or 501 <= npackages:
        print("The number of packages should be more than 100 and less than 500. Bye")
        break
    elif 100 <= npackages <= 200:
        km = 50
    elif 200 <= npackages <= 500:
        km = 60
    print("To which state do you want to send the packages?")
    print("1. " + d1)
    print("2. " + d2)
    print("3. " + d3)
    print("4. " + d4)
    print("5. " + d5)
    print("6. " + d6)
    print("7. " + d7)
    print("8. " + d8)
    print("9. " + d9)
    print("10. " + d10)
    state = input("Select a number: ")

    if state == "1":
        distance = 4486
        cost = km * distance 
        print(f"The shipment of " + str(npackages) + " packages to " + d1 +", has a cost of " + str(cost) + " USD")
        edt(distance) 
    elif state == "2":
        distance = 1754
        cost = km * distance 
        print(f"The shipment of " + str(npackages) + " packages to " + d2 +", has a cost of " + str(cost) + " USD")
        edt(distance) 
    elif state == "3":
        distance = 2623
        cost = km * distance 
        print(f"The shipment of " + str(npackages) + " packages to " + d3 +", has a cost of " + str(cost) + " USD")
        edt(distance) 
    elif state == "4":
        distance = 1271
        cost = km * distance 
        print(f"The shipment of " + str(npackages) + " packages to " + d4 +", has a cost of " + str(cost) + " USD")
        edt(distance) 
    elif state == "5":
        distance = 3927
        cost = km * distance 
        print(f"The shipment of " + str(npackages) + " packages to " + d5 +", has a cost of " + str(cost) + " USD")
        edt(distance) 
    elif state == "6":
        distance = 346
        cost = km * distance 
        print(f"The shipment of " + str(npackages) + " packages to " + d6 +", has a cost of " + str(cost) + " USD")
        edt(distance) 
    elif state == "7":
        distance = 2606
        cost = km * distance 
        print(f"The shipment of " + str(npackages) + " packages to " + d7 +", has a cost of " + str(cost) + " USD")
        edt(distance) 
    elif state == "8":
        distance = 1207
        cost = km * distance 
        print(f"The shipment of " + str(npackages) + " packages to " + d8 +", has a cost of " + str(cost) + " USD")
        edt(distance) 
    elif state == "9":
        distance = 3460
        cost = km * distance 
        print(f"The shipment of " + str(npackages) + " packages to " + d9 +", has a cost of " + str(cost) + " USD")
        edt(distance) 
    elif state == "10":
        distance = 3943
        cost = km * distance 
        print(f"The shipment of " + str(npackages) + " packages to " + d10 +", has a cost of " + str(cost) + " USD")       
        edt(distance) 
    else:
        print("State number not found. Try again")
    continuar = input('Do you want to return to the main menu? Y / N :')

    if continuar.lower() in ["no", "n"]:
        break
