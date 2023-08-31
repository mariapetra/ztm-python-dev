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

two of the same result with for and while:

my_list = [1,2,3]
for item in my_list:
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i+=1

# which is better? for loop = simple / while loop = flexible but be careful of inifinitel loops
# to stop an infinite loop use break

while True:
    input('say something: ')
    break

    or you could break for a conditional:

while True:
    response = input('say something: ')
    if response == 'bye':
        break

# will keep running until you say bye