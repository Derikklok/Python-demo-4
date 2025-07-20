# Python comments
print('Hello World!')

# Python variables
# Python has no specific way to create variables.
# Variables are created when values are assigned to it

num1 = 4 # Int
name = "john" # String
isLoading = True # bool
price = 34.88 # float

print("Integer:\t",num1)
print("String:\t\t",name)
print("Boolean:\t",isLoading)
print("Float:\t\t",price)

print(type(num1))
print(type(name))
print(type(isLoading))
print(type(price))


# Naming conventions for variables
# Can start with underscore character

Name = "sachin"
_name = "pasindu"
print(Name)
print(_name)

# if - else and conditionals

a=7
b=10
if a>b:
    print("A is greater than B")
elif a==b:
    print("A is equals to B")
else:
    print("B is greater than A")