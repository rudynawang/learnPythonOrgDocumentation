# Printing the variables along with the string
first_name = "Rudra"
print("My name is", first_name)
print("My name is"+ first_name)
  ### this method of printing variable can also be said as string formatting
  
print("My name is{}".format(first_name))
print(f"My name is{first_name}")

print(3+2)

print("My name is {}, I'm an Engineer".format(first_name))
print(f"My name is {first_name} Nahawang Pandey")

# String formatting
name = "Rudra"
age = 24
dec_age = 25.5
print("Hello, %s"%name)
print("I am %d years old."%age)
print("My age is %f" %dec_age)
print("My age is %.2f" %dec_age)

# To use two or more argument specifiers, use tuples (parenthesis)
print("Hello, Myself %s and I'm %d years old." %(name,age))

# Any object which is not a string can be formatted using the %s operator as well. The string which returns from the "repr" method of that object is formatted as the string. For example:
num = 3
print("A number: %s" %num)

mylist = [1,2,3]
print("A list: %s" % mylist)

# %x/%X - Integers in hex representation (lowercase/uppercase)

num1 = 11
print("%x -- %X" %(num1,num1))
