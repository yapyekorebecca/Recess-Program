# functions

# example
# functions in python are defined using the 'def keyword
# followed by the function name ,parenthenes{ , inside the parenthenses you pyt a parameter name and  a colon.abs

# example1 
def multiply(a,b) :
    return a*b

result = multiply(5,10)
# print(result)

def get_coordinates():
    return 10,20

x,y =get_coordinates()
print(x,y)

# Exercise 1: Define a function greet with a parameter name , set to 'guest', and print a message
# I am a software programmer


def greet(name='guest'):  
    print("Hello, " + name + "! I am a software programmer.")

greet()      
greet('Yapyeko') 

# Example 3 :Return multiple return values
def get_name_and_position ():
    name='Yapyeko'
    position='I am a software programer'
    return name,position
name,position =get_name_and_position
print(name,position)

# Exercise 4: Return multiple return values of your name and age 
def personal_info():
    name ='Yapyeko'
    age= 25
    return name,age

name,age=personal_info()
print(name,age)


# Notes 
"""_summary_
def : Keyword to defibe a function
function_namr: Name of the function
parameters: Optional,arguments passed t the function 
Docstrings: Optional, describes the dunction purpose
return: Optional, returns a value from the function
    """
    
# syntax for defining a function
# def function_name(parameters):
#     """Docstrings"""
#     function body
#     return value

# Lambda functions 
# they are small anonymous functions defined using the lambda keyword.\
# They are restricted to a single expression

# Syntax for lambda function
# lambda parameter :Expression 

# Example 5 : create a lambda function to add two numbers 
add=lambda a ,b: a + b
print(add(45,70))

# Example 6: Use cases of lambda function for sorting
coordinates = [(1,2),(2,3),(3,1),(5,0)]
print(coordinates)

# Map , filter and reduce
# Example 6: Get the squares of 1 and 5 using map, filter and reduce

number_squares = [1,2,3,4,5]

print(number_squares)

# Exercise 4 : Define a function to get user info that accepts arbitrary keyword arguments and print each 
# key value pair

def get_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

get_user_info(name="Yapyeko", age=25, email="yabecca@gmail.com", Nationality="Zambian")

# Example 7 : How to handle a **kwargs in Functions 

def ahaabwe_function(a, b, **kwargs):
    print(f"a: {a}, b:{b}")

    for key , value in kwargs.items():
        print(f"{key}:{value}")

ahaabwe_function(1,2, x=100, y=200, z=300)