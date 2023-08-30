# while a condition is happening do something

i = 0

# while i < 50:
#     print(i)
# would print an infinite loop as it prints i as long as it is left than 50

while i < 50:
    print(i)
    i += 1
else:
    print('done with all the work')

# this breaks out of the while loop
# why use else? else will only execute if there isnt a break, you wont see this often

