# python was created to keep things simple
# the reason py is so popuar and used to lots of companies
# - external modules
# - we have an entore package system where we can borrow and expand on

# https://docs.python.org/3/py-modindex.html

import random

help(random)
# will tell you what it does

print(dir(random))
# shows all methods available on this package

print(random.random())
print(random.int(1,10))
print(random.choice([1,2,3,4,5]))

from random import shuffle
import random as oolalal
# (can do this to avoid name collisions but always import only what you need)

import sys

print(sys)
# useful - you can do:
sys.argv[0]
# will allow you to access parameters from your terminal

