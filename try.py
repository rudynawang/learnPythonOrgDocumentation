# myint= 4
# print(type(myint))
# if isinstance(myint, int):
#    print("Code Worked")


# mylist = ["ram", "shyam", "hari", "rud"]
# print(mylist.index("hari"))
# print(len(mylist))
# print(len(mylist[0]))
# print(mylist[3].count("r"))





#
print("Hello world!")
x=1
if x==1:
    print("x is equal to 1.")

#
myInt= 7
myFloat=3.4
myI = int(myFloat)
myF = float(myInt)

print(myI)
print(myF)

add = myInt+myFloat
print(add)

str1= "hello"
str2= "world!"
cont = str1 +" "+ str2
print(cont)

num1,num2 = 5,8
print(num1+num2)

#
mylist= []
mylist.append(1)
mylist.append(3)
mylist.append("Ram")
mylist.append("Hari")
print(mylist)
print(mylist[0])
print(mylist[2])

print()

for x in mylist:
    print(x)

print()

#Basic Operators
arith = 1+3-4*5/6
print(arith)

print()

remainder = 22 % 9
print(remainder)

print()

power = 4**2
print(power)

print()

seq= "hello" * 4
print(seq)


#
inte= 18
print("%x" %inte)
print()

#
meList = [3, "ram", 4, "Hari","rudra"]
print(meList[3])
print(meList.index(4))
print(len(meList))
meList.append("Shyam")
print(meList)

print(meList[4].count("r"))
print(len(meList[4]))

print()
str = "Hello world!"
print(str[4])
print(str[1:5])
print(str[:7])
print(str[2:])

print()

print(str[-2])
print(str[-5:-2])
print(str[-4:])
print(str[:-4])
print(str[-3:-5],str)

print()

print(str[::-1])
print(str[::-2])

print()

print(str.upper())
print(str.lower())

print()

print(str.startswith("Hem"))
print(str.endswith("d!"))

print()

print(str.split("l"))



# Common iterable types that work with in :
# List / Tuple / Set:
3 in [1, 2, 3]        # True

# String (checks for substring):
"on" in "John"       # True

# Dictionary (checks keys, not values):
data = {"name": "John", "age": 30}
"name" in data       # True
"John" in data       # False

# Why "John" in data is False
"John" in data   # False
# Even though "John" is a value, it is not a key in the dictionary.
# Since in checks keys only, Python answers False.

# How to check values instead

# If you want to check whether "John" exists as a value, you must explicitly look at the values:
"John" in data.values()   # True

# How to check key–value pairs
("name", "John") in data.items()   # True


# Notes

# Membership checks are case-sensitive
"john" in ["John", "Rick"]  # False

# Using a set instead of a list is faster for large collections:
if name in {"John", "Rick"}:
    

