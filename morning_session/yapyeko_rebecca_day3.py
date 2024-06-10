#python best practices
"""
Follow PEP 8
1.Indentation
2.Maximum Line Lenghth
3.Blank Lines
4.Use meaningful names
6.Use list comprehensions
"""
# Example of a meaningful name
def calculate_area(radius):
    pass


total_price=10000

# # Example of a lazy student with bad meaningfull name
def calc(r):
    pass


tp=10000

# python operators
"""_summary_
Name of Operator         Symbol with example
Addition                       x+y
Subtraction                    x-y
Multiplication                 x*y
Division                       x/y
Modulus                        x%y
Exponentiation                 x**y
Floor Division                 x//y

Example of comparison operator
Name of Operator         Symbol with example
Equal                       x==y
Not equal                   x!=y
Greator than                x>y
Less than                   x<y
Greater than or equla to    x>=y
Less than or equal to       x<=y

Example of python Logical operators 
Name of Operator         Symbol with example
and                         and  
or                          or
not                         not

Examples of membership operators 
Name of the operator       symbol with example
in                          x in y
not in                      x not in y

Example of Bitwise operators 
Name of the operator        Symbol with example
AND                         &
OR                          |
XOR                         ^
NOT                         ~ 

#Python cases
1.snake_case
2.camelCase
3.
4.

"""

# Comprehension (list, dictionary comprehensions)
"""_summary_
comprehension provides a concise way to create lists and dictionaries
what is the symbol for lists and dictionaries 
lists           []square brackets
dictionaries    {}curly brackets 
"""

# Example 1: Basic List comprehensions
# create lists of squares in range of 10
list_squares=[x**2 for x in range(10)]
print (list_squares)

# Exercise 1
even_squares= [x**2 for x in range(20) if x%2==0]
print(even_squares)

# Example 2: Dictionary comprehensions
# create a dictionary comprehension for favourites cars and count the lengths of characters
favorite_cars = ['BWM','Jeep','Mercedes','fordrator']
car_lengths= {car: len(car) for car in favorite_cars}
print(car_lengths)

# Excercise 2 
"""_summary_
Create a list of tuples where each tuple contains
a number and its cube for numbers
between 1 and 10 using a dictionary comprehension
"""


number_dictionary={number:number**3 for number in range (1,11)}
number_cube_list= list(number_dictionary.items())
print(number_cube_list)


