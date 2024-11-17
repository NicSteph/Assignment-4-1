"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
# Charge for this sign.
# Number of characters.
# Color of characters.
# Type of wood.

charge = 0.00
numChars = 18
color = "black"
woodType = "oak"

# Write assignment and if statements here as appropriate.

minCharge = 35.00
minChars = 5 
addChars = 4.00
oakWoodCharge = 20.00 
goldCharge = 15.00

if numChars > 5: 
   totalChars = numChars - 5
   costChars = totalChars * addChars
   charge = minCharge + costChars 

else: 
   charge = minCharge  

if color == "gold": 
   charge = charge + goldCharge 

if woodType == "oak":
   charge = charge + oakWoodCharge 


# Output Charge for this sign.
print("The charge for this sign is $" + str(charge)) 
