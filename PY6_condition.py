#1. Boolean Value/ Boolean Logic/ Boolean Logic Value -> {True, False}
x=3
print(x==3) # x is equal to 3 (True)
print(x==5) # x is equal to 5 (False)
print(x!=1) # x is not equal to 1 (True)
print(x<2)  # x is less than 2 (False)
print(x>2)  # x is greater than 2 (True)
print(x<3)  # x is less than 3 (False)
print(x>3)  # x is greater than 3 (True)

# Note: Variable assignment is done with single equal operator "=" where as comparision is done with double equals operator "=="

#2. Boolean Operators -> {"and", "or"}
name = "Ram"
age = 23
if name == "Ram" and age == 24:
    print("value matched")
else:
    print("Value didn't matched") 

if name == "Hari" or name == "Shyam":
    print("Name is either 'Ram' or 'Hari'")
else:
    print("Name is neither 'Ram' nor 'Hari'")

