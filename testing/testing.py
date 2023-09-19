# A test is simply another py file

# usually you have a test file for each module
# it never runs in prod

# pylint
# pyflakes
# pycharm hsa inbuilt linting
# pep 8
# - these allow us to check for simple styling and mistakes but only goes so far

def do_stuff(num):
    try:
        return int(num) + 5
    except ValueError as err:
        return err
