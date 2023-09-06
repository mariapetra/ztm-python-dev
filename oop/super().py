class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        self.name = name
        self.power = power

class Wizard(User):
    def __init__(self, name, power):
        super()__init__(self, email)
        self.name = name
        self.power = power

    def attack(self):
        # User.attack(self)
        print(f'attacking with power of {self.power}) 

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left- {self.num_arrows}) 


    #instantiate the class

wizard1 = Wizard('merlin', 50, 'wizard@gmail.com')
archer1 = Archer('Robin', 100)
print(wizard1.email)
wizard1.attack()
archer1.attack()

# ```
# - Python has a tool to check if something is an instance of a class:
#     - isinstance(instance, Class)
#     - wizrd1 = Wizard('Merlin', 60)
#     - isinstance(wizard1, Wizard) = True

# Super allows you to use another init from the previous class - we can refer to user without having to pass self
