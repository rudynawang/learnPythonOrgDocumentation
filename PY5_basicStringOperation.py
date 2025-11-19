# Basic String Operation
msg = "Don't over think"
print(msg)

# String Length
str = "Hello world!"
print(len(str))

# character Position 
astring = "Hello world!"
print(astring.index('o'))

### Trying
mylist = ["ram", "shyam", "hari", "rud"]
print(mylist.index("hari"))
print(len(mylist))
print(len(mylist[0]))

# Counting the same character in the string
print(mylist[3].count("r"))

# Printing the slice of the string
astring = "Hello world!"
print(astring[3])     #prints only "l"
print(astring[3:8])   #prints "lo wo"
print(astring[:7])    #prints "Hello w"
print(astring[2:])    #prints "llo world!"

print(astring[-3])
print(astring[-3:])
print(astring[-1:-8])
print(astring[-8:-3])

