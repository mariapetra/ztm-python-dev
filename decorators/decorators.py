@classmethod
@staticmethod

# These are decorators - they have: @name
# - in py functions are first class citizens - they act like variables they can be included in functions
# - underneath the hood they are using the power of functions

def hello():
    print('hellooooo')

greet = hello
del hello

print(greet())
# will work even though delete has removed hello() as greet() still exists