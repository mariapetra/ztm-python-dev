# *args **kwargs
# the * says this can accept any number of positional arguments - can be anything but standard args and kwargs
# kwargs will give you a dictionary

def super_func(*args, **kwargs):
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func(1,2,3,4,5, num1=5, num2=10))
# = 15

# kwargs = add keywords

# rule:

# params, *args, default parameters. **kwargs