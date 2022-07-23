# Define a dictionary
customers = {'06753':'Mehzabin Afroze','02457':'Md. Ali', 
'02834':'Mosarof Ahmed','05623':'Mila Hasan', '07895':'Yaqub Ali'}

# Append a new data
customers['12345'] = 'Craig Damlo'

print("The customer names are:")
# Print the values of the dictionary
for customer in customers:
    print(customers[customer])

# Take customer ID as input to search
idnum = input("Enter customer ID:")

# Search the ID in the dictionary
for customer in customers:
    if customer == idnum:
        print(customers[customer])
        break