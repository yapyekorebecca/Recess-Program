# Dictionaries
# Creating and using dictionaries
# Dictionaries methods and operations
"""_summary_
Dictionaries in python are collections of keys and values 
-Unordered
-Mutable and 
-indexed by keys

"""
# Example 1
# create a dictionary for a student persuing software engineering
# the key must be your name , age , technology interest ,course and year of study 
# put your own details

student_dict={
    'name': 'Yapyeko',
    'age': '23',
    'technology' :'AI',
    'Course': 'BSSE',
    'Year': 'Year3'
}

print(student_dict['Year'])

# Access values

# Modify values 
# Exercise 1: Modify age and technology
student_dict['age'] = 25
print(student_dict['age'])
student_dict['technology']= "Software testing"
print(student_dict['technology'])

# Example2: Adding keys and values
student_dict['email']='yapyekor@gmail.com'
print(student_dict['email'])

# Exercise 2 : remove key and value from tha dictionary
del student_dict['age']
print(student_dict)

# Common Dictionary methods
"""summary
get() // returns the value for the specified key if the key is in the dictionary
if not it returns the default value

update() // Updates the dictionary with the elements from another dictionary

pop() // Removes the specified key and return the corresponding value



"""


# Example 3 :Use the get method to get the value 
print(student_dict.get('technology'))



# Exercise 3 : Use the update method to update to change the value  in age
student_dict.update({'age': '25'})
print(student_dict)
print()

# Exercise 4 : Use the if check t chrck if the age is present in the dictionary
if 'age' in student_dict:
    print(" age is present in the dictionary.", student_dict['age'])
    
else:
    print(" age is not present in the dictionary.")
    
print()

# keys(), and the items () methods

"""_summary_
keys () returns the view of objects that display a list of all keys 
value()returns the view of objects that display a list of values 
items() returns the views of objects that display a list of all keys and value tuple pairs 
"""

# Exercise 5 : Use the update method to change the course and add a new key like ' whatsapp number to the dictioanry'
student_dict={
    'name': 'Yapyeko',
    'age': '23',
    'technology' :'AI',
    'Course': 'BSSE',
    'Year': 'Year3'
}
student_dict.update({'course': 'CSC','whatsapp': '0788888711'})
# print the updated dictionary
print(student_dict)


