import main as mn

WaterRemain=mn.resources["water"]
MilkRemain=mn.resources["water"]
CoffeeRemain=mn.resources["water"]
Money=0


def checkresources(choice):
    if (choice == "espresso"):
        if mn.MENU["espresso"]["ingredients"]["water"] <= WaterRemain and mn.MENU["espresso"]["ingredients"]["coffee"] <= CoffeeRemain:
            CheckMoney(mn.MENU["espresso"]["cost"],choice,mn.MENU["espresso"]["ingredients"]["water"],mn.MENU["espresso"]["ingredients"]["coffee"])
        else:
            if(mn.MENU["espresso"]["ingredients"]["water"] > WaterRemain):
                print(f"There is not enough water for {choice}")

            if(mn.MENU["espresso"]["ingredients"]["coffee"] > CoffeeRemain):
                print(f"There is not enough coffee for {choice} ")
            start()

    elif(choice=="latte"):
        if(mn.MENU["latte"]["ingredients"]["water"]<=WaterRemain and mn.MENU["latte"]["ingredients"]["milk"] <= MilkRemain and mn.MENU["latte"]["ingredients"]["coffee"] <= CoffeeRemain):
            CheckMoney(mn.MENU["latte"]["cost"],choice,mn.MENU["latte"]["ingredients"]["water"],mn.MENU["latte"]["ingredients"]["coffee"],mn.MENU["latte"]["ingredients"]["milk"])
        else:
            if(mn.MENU["latte"]["ingredients"]["water"]>WaterRemain):
                print(f"There is not enough water for {choice}")

            if(mn.MENU["latte"]["ingredients"]["coffee"] > CoffeeRemain):
                print(f"There is not enough coffee for {choice}")

            if(mn.MENU["latte"]["ingredients"]["milk"]>MilkRemain):
                print(f"There is not enough milk for {choice}")
            start()


    elif(choice=="cappuccino"):
        if (mn.MENU["cappuccino"]["ingredients"]["water"] <= WaterRemain and mn.MENU["cappuccino"]["ingredients"]["milk"] <= MilkRemain and mn.MENU["cappuccino"]["ingredients"]["coffee"] <= CoffeeRemain):
            CheckMoney(mn.MENU["capuccino"]["cost"],choice,mn.MENU["capuccino"]["ingredients"]["water"],mn.MENU["capuccino"]["ingredients"]["coffee"],mn.MENU["capuccino"]["ingredients"]["milk"])
        else:
            if (mn.MENU["cappuccino"]["ingredients"]["water"] > WaterRemain):
                print(f"There is not enough water for {choice}")

            if (mn.MENU["cappuccino"]["ingredients"]["coffee"] > CoffeeRemain):
                print(f"There is not enough coffee for {choice}")

            if (mn.MENU["cappuccino"]["ingredients"]["milk"] > MilkRemain):
                print(f"There is not enough milk for {choice}")
            start()
    else:
        print("Invalid choice")
        start()


def CheckMoney(productcost,choice,water,coffee,milk=0):
    global Money
    quaters=.25
    dimes=.10
    nickles=.05
    pennies=.01
    numberofquaters=int(input("Enter number of quaters="))
    quaters=quaters*numberofquaters
    numberofdimes = int(input("Enter number of dimes="))
    dimes=dimes*numberofdimes
    numberofnickles = int(input("Enter number of nickles="))
    nickles=nickles*numberofnickles
    numberofpennies = int(input("Enter number of pennies="))
    pennies=pennies*numberofpennies
    totalmoney=quaters+dimes+nickles+pennies

    if(totalmoney>productcost):
        updateresources(water,coffee,milk)
        Money+=productcost;
        ReturnExtraMoney(totalmoney-productcost)
        DeliverProduct(choice)
    elif(totalmoney==productcost):
        updateresources(water, coffee, milk)
        Money += productcost;
        DeliverProduct(choice)
    else:
        RefundMoney(totalmoney)

def RefundMoney(money):
    print(f"{money} is reunded to the customer")
    start()

def ReturnExtraMoney(money):
    print(F"{money} is returned to the customer")


def DeliverProduct(product):
    print(f"hello user this is your {product} ")
    start()

def updateresources(water, coffee, milk=0):
     global WaterRemain
     global MilkRemain
     global CoffeeRemain
     WaterRemain-=water
     CoffeeRemain-=coffee
     MilkRemain-=milk

def printreport():
    print(f"Water :{WaterRemain}")
    print(f"coffee :{CoffeeRemain}")
    print(f"milk :{MilkRemain}")
    print(f"money :{Money}")
    start()

def start():
    option = input("What would you like? (espresso/latte/cappuccino):")
    if option=="report":
        printreport()
    elif(option=="off"):
         print("Coffee machine is switched off")
    else:
        print("Coming")
        checkresources(option)

start()


# def turnoff():

