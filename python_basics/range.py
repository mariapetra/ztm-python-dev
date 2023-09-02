print(range(100))

# will print:
# range(0, 100)
# not a tuple
# you can iterate over a range so it is good in for loops

for number in range(0, 100):
    print(number)

# stepover:

for number in range(0, 100, 2):
    print(number)

# go backwards:

for number in range(0, 100, -2):
    print(number)

# this will print the range 0 - 10 in 2 lists
for new_list in range(3):
    print(list(range(10)))