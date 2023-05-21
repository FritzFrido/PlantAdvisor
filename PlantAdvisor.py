# PLANT ADVISOR PLANT ADVISOR PLANT ADVISOR PLANT ADVISOR PLANT ADVISOR PLANT ADVISOR PLANT ADVISOR PLANT ADVISOR

# (Get Input) Ask users if they want to check which plants go in which plot OR if they want to check out the Planting Buddy

def main():
    from time import sleep
    print("Welcome! I am your Growy, your plant advisor. I'd like to help you decide which plot is best for your plants and whether they will fit together!")
    print("")
    sleep(1.5)
    action = input("Would you like to find the ideal home for your plant? (Enter \"A\") or do you want to know which plants are best buddies? (Enter \"B\")")
    print("")
    print("")

    if action == "A":
        PlantPlace()
    else:
      PlantingBuddy()


# Define the PlantPlace und TellPlot as functions with conditionals

# Define PlantPlace

def PlantPlace():
    from time import sleep
    sleep(0.5)
    print("Super! Let’s find the best place for your plant!")
    print("")
    sleep(1.0)
    AskLight = input("Lets get to know your plant better: Does it need much, normal or less sunlight? ")
    print("")
    sleep(1.0)
    AskWater = input("Does your plant need lots, normal or fewer amounts of water? ")




# Ask user for the different characteristics of the plant they would like to plant 

# Ask-Light: Sun / MidShad / Shad (Define Categories)
# Ask–WaterNeed: Few / Mid / Much (Define Categories)



# Define the TellPlot function with conditionals

# def TellPlot():

# Define the PlantingBuddy function with conditionals

# def PlantingBuddy():
   # print("Good choice! I'm your Planting Buddy: I'll tell you which plants will happily grow to gether and which might challenge each other!")




main()
