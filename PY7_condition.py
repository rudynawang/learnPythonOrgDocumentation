#1. Boolean Value = {True, False/ 1,0 / Yes,No / On,Off}
#   Boolean Logic = {(AND/^),(OR/v),(NOT/¬)}
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

#3. The 'in' operator
num1 = 3
nums = [1,2,3]
if num1 in nums:
    print("number exits in the list")
else:
    print("number does not exist in the list")


num = 2
if num < 0:
    print("number is negative")
elif num > 0:
    print("number is positive")
else:
    print("number equals to Zero")


st1 = False
st2 = True
if st1 is True:
    print("st1 is True")
elif st2 is True:
    print("st2 is True")
else:
    print("Neither st1 nor st2 is True")
    