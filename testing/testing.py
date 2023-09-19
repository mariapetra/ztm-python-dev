# A test is simply another py file

# usually you have a test file for each module
# it never runs in prod

# pylint
# pyflakes
# pycharm hsa inbuilt linting
# pep 8
# - these allow us to check for simple styling and mistakes but only goes so far

# https://docs.python.org/3/library/unittest.html

def do_stuff(num=0):
    try:
        if num:
        return int(num) + 5
    else:
        return 'please enter number'
    except ValueError as err:
        return err
