# Error Hnadling in Python
# Exception Hnadling with try, except , else , and finally 
# custom exceptions 

"""_summary_
Notes:
Error handling in python it helps t handle unexpected situations and errors

1.Try: contains code that might throw an exception
NB: if an exception occurs , the rest of the code in the try block is skipped or ignored 

2.Except: catches and handles the exceptions
NB: You can specify different handlers for different exception types 

3.Else : the code runs if no exception occurs 
if no exceptions are raised in the try block it runs.

4.Finally: it runs whether an exception is raised/ocured or not 
NB: Used for cleaning up actions that 

"""
# Example 1 : Handle exceptions with division by zero.

try:
    number = int(input('Enter a number: '))
    result =20/number
    
except ValueError:
    print ("Invalid number! Please enter a valid number ")

except ZeroDivisionError:
    print("Error! Division by zero is not allowed")
    
else:
    print(f"Result is {result}")

finally:
    print("Excecution completed sucessfully")
    
# Exercise 1: write a function that converts a string into an integer and handle both value error
# if the string can not be converted as an integer and the TypeError if the input is not a string 
# use multiple except block to handle this exceptions

def string_to_integer(s):
    try:
       
        if not isinstance(s, str):
            raise TypeError("Input must be a string")
        
    
        result = int(s)
    
    except ValueError:
        print("Could not convert the string to an integer.")
    
    except TypeError as e:
        print(f"Type error: {e}")
    
    else:
        print(f"Conversion successful: {result}")
    
    finally:
        print("Conversion attempt completed.")


# Custom exception handling 
# Example 2: Exception raised for error in the input , ifi funds are insufficient

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
       self.balance=balance
       self.amount=amount
       self.message=f"Attempt to withdraw {self.amount }with only {self.balance} in account"
       super().__init__(self.message)
       
       
def withdraw (balance,amount):
    if amount > balance:
        raise InsufficientFundsError(balance,amount)
    return balance-amount

# custom exception handling
try:
    balance=20000
    amount_to_withdraw=100000
    new_balance= withdraw(balance,amount_to_withdraw)

except InsufficientFundsError as e:
    print('Error: ')
    
else: 
    print("Withdraw")

finally:
    print("Transaction completed")

# Note
"""_summary_
Defining a custom exception

Class CustomError (Exception):
 #Custom Execption for specific error cases
 
def __init__(self, ,massage):
  super().__init__(message)
  self.message=message
  
###Raising a custom exception
   define check _value(Value):
      if Value is < 0 or value:
        raise CustomError ("Value cannot ")
        return value

        
# Handle exceptions with try, except, else, and finally
    try:
        result = check_value(-10)
        
    except CustomError as e:
        print(f"Custom error caught: {e.message}")
"""
# Exercise 2: Create a custom exception InvalidAgeError and write a function that raises
#this exception if the given age is negative .Handle this custom exception when calling the function 



class InvalidAgeError(Exception):
    def __init__(self, message="Age cannot be negative"):
        self.message = message
        super().__init__(self.message)

# SOLN 1
def validate_age(age):
    try:
        if age < 0:
            raise InvalidAgeError()
        
       
        print(f"Age {age} is valid.")
    
    except InvalidAgeError as e:
        print(f"InvalidAgeError: {e}")
    
    finally:
        print("Validation completed.")

# SOLN 2
def check_age():
    age = int(input("Enter your age: "))
    if age < 0:
        raise InvalidAgeError(age)
    else:
        print(f"Age is {age}")

try:
    check_age()
except InvalidAgeError as e:
    print(e.message)
else:
    print("Valid age entered.")
finally:
    print("Age check complete.")



   
        