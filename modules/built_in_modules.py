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

# specialized data types

from collections import Counter, defaultdict, OrderedDict
# capitals = class / no capitals = func

li = [1,2,3,4,5,6,7,7]
print(Counter(li))
# will create a dict

sentence = 'b;ah blak oskjrkff ugug'
print(Counter(sentence))
# will print a set of how many time each letter is in sentence

# defaultdict - will give you a default value if something does not exist
# ordereddict - will retain the order that you insert into a dict - not required from 3.7 dicts are now ordered by default
# https://softwaremaniacs.org/blog/2020/02/05/dicts-ordered/en/

# https://stackoverflow.com/questions/176011/python-list-vs-array-when-to-use

from datetime
from time import time
from array import array

# lists in python are called arrays in other lang sometimes
# arrays take up less memory and perform faster
# tell it what type of data it will hold

arr = array('i', [1,2,3])

(datetime.time(5,45,2))
# will create time object

datetime.date.today()
# will add todays date