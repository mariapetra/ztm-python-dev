# oop
# - should be singular - character not characters
# init is a special method - dunder/magic method
# Conctructor method - called whenever we instantiate
# What is self? A way to define self - refers to the player character
# so self = the class itself
# self = whatever is to the left of the dot
# we can have a reference to something that isnt created yet
# CAN WRITE CODE ONCE - MAKE DYNAMIC - CHANGE BASED ON WHAT WE GIVE IT
# name and age are attributes
# an object - player - has an attribute - name
# They can be accessed by using the . eg player1.age
# if i print player1 . player2 they will be created at different places in memory
# this keeps things safe


class PlayerCharacter:
    #class object attribute
    # not dynamic actual attribute on the class
    # this will be true for all objects
    # we can use anywhere
    membership = True
    # __init__ = constructor
    def __init__(self, name='anyonymous', age=0):
        if (PlayerCharacter.membership and age > 18):
            self.name = name
            self.age = age


    def shout(self):
        print(f'my name is {self.name}')

    #decorator
    #what does this classmethod do?
    @classmethod
    adding_things(cls, num1, num2):
        return num1 + num2

player1 = PlayerCharacter('Maria', 38)
player1 = PlayerCharacter('Tom', 27)

print(player1.run())
print(player2.age)
print(player1.adding_things(2,3))

    # @classmethod
    # adding_things(num1, num2):
    #     return num1 + num2
# returns error - takes 2 positional arguments but 3 were given
# thats because adding_things is cls (Class) so we update adding_things to include itself (cls)

#we can use this without instantiating a class - it is a class method

print(PlayCharacter.adding_things(2,3))
#print(CLass.method(attribute,attribute))

# classmethods are not used often but there are cases where it may e usesful eg use cls to instantiate something:
        # @classmethod
        # adding_things(cls, num1, num2):
        #     return ('Teddy',num1 + num2)

        # player3 = PlayerCharacter.adding_things(2,3)
        # we have just made teddy aged 5

#another way is a static method which works the same way accept you do not have access to the cls
# eg you could add things but not create the name 0 use this when we dont care about the class state/attributes

@staticmethod
def adding_things2(num1, num2):
    return num1 + num2