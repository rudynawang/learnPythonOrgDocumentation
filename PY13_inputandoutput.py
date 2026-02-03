#1. Input() Function
print("Enter anything as input:")
astr = input()
print("You have typed:",astr)


# converting input into our required datatypes using functions like int(),float(),str()

num = int(float(input()))
print(num)
print()

flo = float(input())
print(flo)
print()

st = str(input())
print(st)
print()


# how to take two or more data types as input from a single line separated by spaces?
# Here we make use split() and map() functions

a, b = map(int, input().split())
array = input().split()
add =0
for each in array:
    add = add +int(each)

print(a, b, add)