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

print(astring[-3])    # (-ve) number leads starting from the end of the string and -3 denote third character starting from the end of the string
print(astring[-3:])   # prints from third character from the end to the end of the string
print(astring[:-3])   # prints from very begining of the string to the position one less than the number mention in the index i.e upto -4th position character form the end 
print(astring[-1:-8]) # XXX doesnot print anything / doesn't work
print(astring[-8:-3]) # prints the slice of the string from -8 position to the -3 position conting form the first position of the end of the string 

print(astring[1:9:1]) # prints slice of the string as same does by "astring[1:9]", since [1:9:1]- denotes [start:end:step] and the step (:1) is like zero step 
print(astring[1:9:2]) # prints slice of the string by skipping one character from the starting position i.e 1th index

# Reversing the string like this
print(astring[::-1])  # prints the reverse of the string without skipping the character 
print(astring[::-2])  # prints the reverse slice of the string by skipping the one character 

# Converting the string into Lower and Upper Case
str1 = "I LoVe BuTwaL"
print(str1.upper())
print(str1.lower())


print(str1.startswith("end"))
print(str1.endswith("butwal"))

