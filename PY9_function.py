#1. Simple function defining in Python using block_head "def" and block_name "my_function"
def my_function():
    print("Hello From My Function")

my_function() # function calling (without calling the function it will not be executed.)


#2. Defining function with arguments
def my_function_with_arguments(username,greetings):
    print("Hello, %s, From My Function!, I wish you %s" %(username, greetings))

my_function_with_arguments("Rudra","Good Morning!")

