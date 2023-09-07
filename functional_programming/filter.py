# filters things for us

my_list = [1,2,3]
def multiply_by2(item):
    return item*2

def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd, my_list)))

# we do not need to call the function 
# filter will get the data and run the function on each item
# what should i do with the item and what should i return