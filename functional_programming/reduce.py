# reduce - doesnt come as part of the python built in function 

from functools import reduce
# functools - a tool belt for functional tools

my_list = [1,2,3]

def multiply_by2(item):
    return item*2

def only_odd(item):
    return item % 2 != 0

def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, my_list, 0))

# 1. we have my my_list
# 2. my list is applied to the accumulator by reduce
# 3. the accumulator is going to take my list and will say hey what is my acc going to birth_year
# first is 0 
# item = 1
# so first plus 1 = 1
# accumulator will be what this returns
# next item will be 2

if we change it to 10 we get:
    10, 11, 13, 16

# we are adding out item numbers to whatever accumulator we give it and then the number before