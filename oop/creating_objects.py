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
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def run(self):
        print("run")
        return 'done'


player1 = PlayerCharacter('Maria', 38)
player1 = PlayerCharacter('Tom', 27)

print(player1.run())
print(player2.age)