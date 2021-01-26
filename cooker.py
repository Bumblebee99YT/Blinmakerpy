# variables
eggsAmount = 0
eggsMin = 1
milkAmount = 0
milkMin = 200 #ml
flourAmount = 0
flourMin = 100 # grams

username = input("What is your name: ")
print('Hello ' + username)
print("Blinmaker is starting...")

# Input of items available

# egg
eggsAmount = input("How many eggs do you have? ")
# print("You have " + eggsAmount + " eggs.")

# Milk
milkAmount = input("How much milk do you have? (milliliter)")
# print("You have " + milkAmount + " ml milk.")

# flour
flourAmount = input("How much flour do you have? (grams)")
# print("You have " + flourAmount + " g flour.")

# main code here
if ((int(eggsAmount)) < (int(eggsMin)) or (int(milkAmount)) < (int(milkMin)) or (int(flourAmount)) < (int(flourMin))):
  print("No blin today :(")
else:
  flourAmount = int(flourAmount) / int(flourMin)
  print("you have " , int(flourAmount) , " portions of flour")

  milkAmount = int(milkAmount) / int(milkMin)
  print("you have " , int(milkAmount) , " portions of milk")

# find smallest number of all 3

if (int(eggsAmount) <= int(milkAmount) and int(milkAmount) <= int(flourAmount)):
  smallest = eggAmount
elif (int(milkAmount) <= int(flourAmount) and int(milkAmount) <= int(eggsAmount)):
  smallest = milkAmount
else:
  smallest = flourAmount

# more stuff

print(" ") # every portion is 4 blins
print("You can make " , int(smallest) * 4 , " of blins.")
print(" ")
print("You will need ", int(smallest) * int(eggsMin) , "eggs")
print("You will need ", int(smallest) * int(milkMin) , " ml of milk")
print("You will need ", int(smallest) * int(flourMin) , "g of flour")
print(" ")
print("Blinmaker is shutting down...")