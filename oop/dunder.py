# __ are special methods
# - they allow us to use python specific functions on our class
# 

class Toy():
    def __init__(self, color, age):
        self.color = color
        self. age = age
        self.my_dict = {
            'name': 'yoyo',
            'has_pets': False
        }
    
    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __delete__(self):
        return 'deleted'

    def __call__(self):
        return('yes??')

    def __getitem__(self, i):
        return self.my_dict[i]

action_figure = Toy('red', 0)
action_figure.__str__()
# is the same as str

# https://docs.python.org/3/reference/datamodel.html#special-method-names