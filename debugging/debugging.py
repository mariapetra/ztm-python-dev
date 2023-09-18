# good practices

# use linting
# what is linting?
# allows us to detect issues with our code

# pycharm already has linting in
# always use ide or editor - auto formatting - detects errors

# learn to read errors

# pdb - python debugger - https://docs.python.org/3/library/pdb.html

import pdb
# instead of print
# https://docs.python.org/3/library/pdb.html

def add(num1, num2):
    pdb.set_trace()
    return num1 + num2

add(4, 'hhjhgjhg')

# type help in terminal and it will give everything it has
# step allows you to go to line by line
# a = all arguments
# w = context of current line
# continue = continue
# then exit
# you can also change variables within here to test changing things to another value