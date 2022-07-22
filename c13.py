# Import re module
import re

# Take any string data
string = input("Enter a string value: ")
# Define the searching pattern
pattern = '^[A-Z]'

# match the pattern with input value
found = re.match(pattern, string)

# Print message based on the return value
if found:
  print("The input value started with a capital letter")
else:
  print("You have to type a string that starts with the capital letter")