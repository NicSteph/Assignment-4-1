"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
charge = 35.00
numChars = 18
color = "black"
woodType = "oak"

# Write assignment and if statements here as appropriate.
if numChars > 5:
  charge = charge + (numChars - 5) * 4
if woodType == "oak":
  charge = charge + 20
if color == "gold":
  charge = charge + 15

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
