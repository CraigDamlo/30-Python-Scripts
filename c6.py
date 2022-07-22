import random

# Assign a numeric value
number = random.randrange(0,100)

# Check the is more than 70 or not
if (number >= 70):
    print("You have passed with %d" % (number))
else:
    print("You have not passed witn %d" % (number))
