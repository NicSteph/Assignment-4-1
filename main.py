"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
charge = 35.00
numChars = 8
Color = "gold"
woodType = "oak"

# Write assignment and if statements here as appropriate.
if numChars > 5:
  charge = charge (numChars - 5) *4
# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
