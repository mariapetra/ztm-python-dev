class User():

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

    def run(self):
        print('ran really fast')

class HybridBorg(Wizard, Archer)
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, arrows)


hb1 = HybridBorg('borgi', 50, 100)
print(hb1.run())
print(hb1.attack())