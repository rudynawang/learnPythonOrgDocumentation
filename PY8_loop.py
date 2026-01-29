# For Loop
nums= [9,8,7,6,5,4]
for x in nums:
    print (x)

print()

for index, value in enumerate(nums):
    print(index, value)

print()

# For Loop using "range" and "xrange" function

for i in range(5):
    print(i)

print()

for i in range(2,5): # having starting and ending value {range(start,end)}
    print(i)

print()

for i in range(2,9,2): # having start, end and step value {range(start,end,step)}
    print(i)

print()

# While Loop

count = 0
while count<7:
    print(count)
    count+=1

    
