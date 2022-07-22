import math
# Assign values to x and n
x = 4
n = 3
x2 = 3.14
n2 = 2

# Method 1
power = x ** n
print("%d to the power %d is %d" % (x,n,power))

# Method 2
power = pow(x,n)
print("%d to the power %d is %d" % (x,n,power))

# Method 3
power = math.pow(x2,n2)
print("%.2f to the power %d is %.2f" % (x2,n2,power))