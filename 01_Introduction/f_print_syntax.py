"""
Purpose: print() function syntax and usage
"""

name = "Almighty" #str

print("name=", name)
print("Name of student is name")

#         str             str
print("Name of student is" +  name)
print("Name of student is" +  name)
print()

print("Name of student is", name)
print("Name of student is", name, sep=" ")
print("Name of student is", name, sep=" ")
print("Name of student is", name, sep=" ")


print(1, 2, 3, 4, 5, 6) # default sep=' '
print(1, 2, 3, 4, 5, 6, sep=" ")
print()

print(1, 2, 3, 4, 5, 6, sep="~")
print(1, 2, 3, 4, 5, 6, sep="_")
print(1, 2, 3, 4, 5, 6, sep=":")
print()

#NOTE: Python is dynamic typed language 
name = 1232
print("Name of student is", name)

# #        str             int
print("Name of student is" + name)

#NOTE: Python is strictly typed language
print("1 + 2      =", 1 + 2) # addition
print("'1' + '2'  =", "1" + "2") # string concatenation
print()

# 1 + '2' # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# type converters - str(), int(), float()
print("1 + INT('2') =", 1 + INT("2"))
print("str(1) + '2'=", str(1) + "2")

print()
print("int('234')   =", int("234"))

# print("int('23.4')  =", int('23.4')) # ValueError: invalid literal for int
# print("int('two')  =", int('two')) # ValueError: invalid literal for intprint("Name of student is", name)

print("Name of student is" + str(name))
print("Name of student is"+ " " + str(name))