items = str("House      Sq.mts.  Bedrooms  Bathrooms")
home1 = str("  1          200        3         2") 
home2 = str("  2          150        2         2")
home3 = str("  3          100        2         1") 
home4 = str("  4          100        1         2")
home5 = str("  5           80        1         1")
costs = str("          x 90 USD   x 40 USD  x 30 USD")

def homenumber(home): 
    print(items)
    print(home)
    print(costs)
    print("Subtotal: $", int(home.split()[1])*90,"   + $", int(home.split()[2])*40,"   + $", int(home.split()[3])*30)
    print("Total: $", int(home.split()[1])*90 + int(home.split()[2])*40 + int(home.split()[3])*30)

while True:
   

    print("Welcome to Real State Rent System")
    print("There are 5 houses for rent: ")
    print(items)
    print(home1)
    print(home2)
    print(home3)
    print(home4)
    print(home5)
    nhome = int(input("Enter the house number to get the price: "))

    if nhome == 1:
        home = home1
        homenumber(home)
    elif nhome == 2:
        home = home2
        homenumber(home)
    elif nhome == 3:
        home = home3
        homenumber(home)
    elif nhome == 4:
        home = home4
        homenumber(home)
    elif nhome == 5:
        home = home5
        homenumber(home)
    else:
        print("Number not found")
    continuar = input('Do you want to return to the main menu? Y / N :')

    if continuar.lower() in ["no", "n"]:
        break


        
    