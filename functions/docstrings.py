# unique thing we can do with functions allows us to comment inside of a function in a way that other people can know what it is doing
# if you hove over the func it will tell you what is in the docstrings

def test(a):
    '''
    This funtion tests and prints param a
    '''
    print(a)

help(test)
# help also finds out what a function does

print(test.__doc__)
# will print info of the docstrings