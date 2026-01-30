#1. Simple function defining in Python using block_head "def" and block_name "my_function"
def my_function():
    print("Hello From My Function")

my_function() # function calling (without calling the function it will not be executed.)


#2. Defining function with arguments
def my_function_with_arguments(username,greetings):
    print("Hello, %s, From My Function!, I wish you %s" %(username, greetings))

my_function_with_arguments("Rudra","Good Morning!")

#3. Function may return a value to the caller, using the keyword- "return"
def sum_two_numbers(a,b):
    sum = a+b
    return sum

add = sum_two_numbers(5,6)
print("The sum of two numbers is: %d" %(add))


#4. Exercise

def list_benefits():
    return ["More organized code","More readable code","Easier code reuse","Allowing programmers to share and connect code together"]

def build_sentence(benefit):
    return (benefit+" is a benefit of functions!")

def name_the_benefits_of_functions():
    list_of_benefits= list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()