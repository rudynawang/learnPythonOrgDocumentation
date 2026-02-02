#1. A Dictionary is a data type similar to arrays, but works with keys and values instead of indexes.
#   Database of phone numbers could be stored using a dictionary like this:

phonebook = {}
phonebook["John"] = 9876543223
phonebook["Ram"] = 9853478732
phonebook["Hari"] = 9843258729
print(phonebook)
print()

#2. Next way, a dictionary can be initialized with the same values in the following notation:
phonebook = {
    "John" : 9876543223,
    "Ram" : 9853478732,
    "Hari" : 9843258729
}

print(phonebook)
print()

#3. Iterating over Dictionaries
phonebook = {
    "Rudra" : 9876543223,
    "Krishna" : 9853478732,
    "Maruti" : 9843258729
}

for name, phonenumber in phonebook.items():
    print("Phone number of %s is %d" %(name, phonenumber))
print()

#4. Removing a value from the Dictionaries
phonebook = {
    "John" : 9876543223,
    "Ram" : 9853478732,
    "Hari" : 9843258729
}

del phonebook["John"]
print(phonebook)
print()

#5. Next way to Remove the value/item from the Dictionaries
phonebook = {
    "John" : 9876543223,
    "Ram" : 9853478732,
    "Hari" : 9843258729
}

phonebook.pop("Hari")
print(phonebook)