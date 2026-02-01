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

print()

# Break and Continue Statement
# Break:
count = 0
while(1):
    print(count)
    count+=1
    if count>=5:
        break
    
print()
# Continue:
for x in range(11):
    if x%2==0:
        continue
    print(x)

print()

# We can use "else" part in the loops.
# In While Loop
count = 0
while count<5:
    print(count)
    count+=1
else:
    print("count value reached %d" %count)

print()

# In For Loop

for i in range(1,10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for " \
    "loop is terminated because of " \
    "break but not due to fail in condition")




