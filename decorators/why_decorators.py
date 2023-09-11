# 1. supercharges our function

def my_decorator(fun):
    def wrap_func():
        func()
    return wrap_func()

@my_decorator
def hello():
    print('hellooooo')

# why do this? the decorator hasnt changed anything
# it works as expected but what it allows us to do is now we can add extra functionality

def my_decorator(fun):
    def wrap_func():
        print('*****')
        func()
        print('*****')
    return wrap_func()

@my_decorator
def hello():
    print('hellooooo')
@my_decorator
def bye():
    print('see you later')
# will now print:

# *****
# hellooooo
# *****

# how does it do this?

# all we are doing is:

# calling hello and wrapping it with my_decorator so hello2 = my_decorator(hello)