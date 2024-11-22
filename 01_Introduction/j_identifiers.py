"""

purpose: Ientifier in Python 

    Variable 
    
          1. keyword --> words which have some meaning
          2. Identifier --> words which are defined by 


"""
#Loading a module 
import keyword

print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async',
# 'await', 'break', 'class', 'continue', 'def', 'elif', 'else',
# 'except', 'finally', 'for, 'from', 'global', 'if', 'import', 
# 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']
print()

print(True) # True
# print(true) NameError: name 'true' is not defined.

my_value = "something"
print(my_value)  # Identifier

# True = "something"
# SyntaxError: cannot assign to True

print(keyword.iskeyword("True"))        # True
print(keyword.iskeyword("true"))        # False
print(keyword.iskeyword("my_value"))    # False

#-----------------------------------------------
# Identifiers - User-defines variables
#  - Naming convention
#      1. Keywords should not be used as identifiers
#      2. first character: a-z, A-Z, _
#      3. remaining char: a-z, A-Z, _ , 0-9

#---- Rule 1
# True = 123 # SyntaxError: cannot assign to True
# None = 'Nothing' # SyntaxError: cannot assign to None 

#PEP 8 - Dont create identifiers which are similar
true = 123
none = "Nothing"

true_value = 123
none_result = "Nothing"

# ---- Rule 2 & 3
name = "Shirisha"
Name_of_student = "Shirisha"
first_name = "Shirisha"
student_1 = "Shirisha"
class_02_a = "Python comment operations"
first____child = "Satvik"

# PEP 8 recommends to use capitals for constants
PI = 3.1416
DOZEN = 12

# name = "Shirisha"
# Name-of-student = "Shirisha"
# Nameof student = "Shirisha"
# 1st_name = "Shirisha"

_2nd_student = "Someone"

_job = "software development"
__role = "product support"
___salary = 123123123123123123123



# OOP -> name mangling
# variable  -> public variable
# _variable -> protected variable
# __variable -> private variable

# __variable__ -> Built-in functions
# Ex: __file__, __name__, __doc__, __dict__, __init__

print("__name__ =", __name__) # __main__
print("__file__ =", __file__)

# print("__Shirisha__=", __Shirisha__)
# NameError: name '__Shirisha__' is not defined

# Python is case-sensitive language
animal = "DOG"
print(animal)

# print(Animal)
# NameError: name 'Animal" is not defined. Did you mean

ANIMAL = "PIG"
print(ANIMAL)

Animal = "Camel"
print(Animal)


#---------------------------
# variable casing 
# 1.snake casing or underscore casing

student = "Shiva"
employee_salary = 2344536374.76
cost_of_mango = 12
selling_price_of_apples = 34

output_of_thermal_sensor = 32
no_of_current_processes = 5


# 2. Camel casing 
Student = "Shiva"
EmployeeSalary = 2344536374.76
CostOfMango = 12
SellingPriceOfApples = 34

OutputOfThermalSensor = 32
NoOfCurrentProcesses = 5

