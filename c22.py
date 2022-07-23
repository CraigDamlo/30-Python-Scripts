# Define addition function
def addition(number1, number2):
    result = number1 + number2
    print("Addition result:",result)

# Define area function with return statement
def area(radius):
    result = 3.14 * radius * radius
    return result  

# Call addition function
input1 = int(input("First Number: "))
input2 = int(input("Second Number: "))
addition(input1, input2)
# Call area function
radinput = int(input("Radius: "))
print("Area of the circle is",area(radinput))