

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

what if we want to call another argument within the top function?

# decorator pattern
# gives decorator flexibiliyty - can pass as many args as we want into our function and then unpack them
def my_decorator(fun):
    def wrap_func(*args, **kwargs):
        print('*****')
        func(*args, **kwargs)
        print('*****')
    return wrap_func()

@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)

a = my_decorator(hello)
a('hiiiiiii', ':)')

# but why do we need them? 
# - we have a decorator below which will be able to test how well performing my functions are just by adding @performance
# - another good use could be authenticated

# Decorator
from time import time
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'it took {t2-t1}s')
        return result
    return wrapper

@performance
def long_time():
    for i in range(1000000):
        i*5