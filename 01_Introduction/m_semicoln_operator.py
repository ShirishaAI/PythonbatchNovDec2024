"""

Purpose: Multiple statements in same line
     ;logic separator
     ;statement completion operator
"""

print("Hello" "World")
print("Hello", "World")

print("Hello", 21312)
# print("Hello" 21312)
# SyntaxError: invalid syntax. Perhaps you forgot a comma?

print("Hello", 21312, 213, 123, + 123 -3)
print()

# Semicoln operator

# Method 1
num1 = 100 
num2 = 200
sum_of_numbers = num1 + num2 
print("Sum of Number:", sum_of_numbers)

# Method 2 using ; operator 
num1 = 100; num2 = 200; sum_of_numbers = num1 + num2; print("Sum of Number:", sum_of_numbers)

# Conclusion
# 1. ; is optional. Will not change anything 
# 2. ; is important if we need write more than one statement in same
# 3. Unecessarily placing semicolon at end of statementwill increase

"""
python -c "print('hello world')"

python -c "num1 = 123; num2 = 300; sum_of_numbers = num1 + num2; print("Sum of Number:", sum_of_numbers)


language
    - scripting language Ex: batch, shell, .....
    - General Purpose programming language Ex: c, c++, java,

Python is both scripting and General purpose programming language


.bat
    cd directory1
    cd subdirectory2
    ping google.com > result.txt
"""