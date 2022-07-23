# Define the string 
string = 'Python Bash Java Python PHP PERL'
# Define the search string 
search = (input("Enter a search:"))
# Store the count value
count = string.count(search)
# Print the formatted output
print("%s appears %d times" % (search, count))