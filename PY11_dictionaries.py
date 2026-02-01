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