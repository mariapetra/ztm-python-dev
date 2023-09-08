# - one time anonymous functions that you dont need more than once
# useful when you are using them for functions that 
#     a. you only use once
#     b. anonymous functions - we dont need to store them anywhere on our machines

# lambda param: action(param)

from functools import reduce
# functools - a tool belt for functional tools

my_list = [1,2,3]

print(list(map(lambda item: item*2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda item: acc, item: acc+item, my_list)))
# will replace:

# def multiply_by2(item):
#     return item*2

# once this is run it is forgotten about
# code = small but less readable - dont confuse others - be careful