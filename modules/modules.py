# how to organise code

# py file
# function
# class
# functional programming
# keep code clean, maintainable and organised

# problem - everything is contained in one file
# in real life this isnt the case 

# say we have multiple files, can we link all of the files together?
# yes - modules

# - modules are .py files
# buy building modules we can have different files to divide up our code

# one of the most common ways is to create a utility.py

def multiple(num1, num2):
    return num1+num2

def divide(num1, num2):
    return num1/num2

# say the above code is in utility.py

# we have another file called main.py:

import utility

# this will create pycache - pyc
# it is a compiled file
# instead of loading utility.py it will load the cache version
# if we change it the pyc will be rerun as we have a different file
# we do not touch this it just comes under the hood



