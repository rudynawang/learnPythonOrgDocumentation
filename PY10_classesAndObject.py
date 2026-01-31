#1. A very basic class would look something like this.
class Myclass:
    varA = "First class"

    def firstclass(slef):
        print("This is the first class")

#2. Creating an object in Python / Assigning the above class(template) to an object.
class Myclass:
    varA = "First class"

    def firstclass(self):
        print("This is the first class.")

firstobject = Myclass() # variable "firstobject" holds an object of the class "Myclass" that contains the variable and the function defined with in the class "Myclass"


#3. Accessing the Object Variable.
class Myclass:
    varA = "First class"

    def firstclass(self):
        print("This is the first class.")

firstobject = Myclass()

firstobject.varA # This is how we access object variable from the class "Myclass"


#4. Now printing the "Myclass" class variable accessed through the class object "firstobject".
class Myclass:
    varA = "First class"

    def firstclass(self):
        print("This is the first class.")

firstobject = Myclass()

print(firstobject.varA)
print()



#5. Multiple different objects can be created that are of the same class "Myclass" (those different objects can have the same variables and the functions defined with in the class.)
#   However each object contains independent copies of the variables defined in the class.
#   If we were to define another object with the "Myclass" class and then change the string in the variable as shown in below:
class Myclass:
    varA = "First class"

    def firstclass(self):
        print("This is the first class.")

firstobject = Myclass()
secondobject = Myclass()

secondobject.varA = "String Changed"

print(firstobject.varA)
print(secondobject.varA)
print()


#6. Accessing the object Function.
class Myclass:
    varA = "First class"

    def firstclass(self):
        print("This is the first class.")
        
firstobject = Myclass()
secondobject = Myclass()

firstobject.varA = "New String created"
print(firstobject.varA)
secondobject.firstclass()
print()


#7. "init()" function is a special function that is called (while creating the object of the class / when the class is being initiated.
#    it is used for assigning the values class.

class NumberHolder:
    def __init__(self, number):
        self.number = number

    def returnNumber(self):
        return self.number
    
obj = NumberHolder(5)
print(obj.returnNumber())
