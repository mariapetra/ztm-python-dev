4 pillars of OOP - in any language not just python
the 4 things OOP does really well

1. encapsulation - is the binding of data and functions that manipulate that data
    - we encapsulate into one big obj so we keep everything in this box that users or cide or other machines can interact with
    eg the player object instead of using variables for name/age 
    - attributes and methods

    why?
        - extra power
        - imagine we had methods without attributes
        - would be llike a dictionary - coudnt do anything to it
        - with a class you can package things into instances
        - they have meaning

2. Abstraction - means - hiding of information - or abstracting away information and giving access to only whats neccasary - everything else we hide under the hood / like under a blanket

    - what does this mean?
    - in the player class - we run player.speak we dont need to know how it is working we just know it works
    - sometimes we just need to get the method/attribite - len - abstractes away how it works we just know it works
    - we dont always need to code from scratch
    - we dont care how it has been implemented
    - same as a tuple


    #Public vs Private Variables

        - We hide info and only give access to things a user in concerned about
        - we shouldnt hve access to init / name / age
        - can we make a private variable?
            - Not in Python
        - So we do _name or _age
            - This is a convention - as Python programmers we know that if we see underscore it is a private variable
            - You can overwrite them but you should know not to touch this

3. Inheritance - allows new objects to take on the properties of existing objects 
    - You can inherit classes
    - The below example shows how all users will inherit signin from the User class - they inherit the user class

    eg:
    ```
    class User:
        def sign_in(self):
            self.name = name
            self.power = power

    class Wizard(User):
        def __init__(self, name, power):
            self.name = name
            self.power = power

        def attack(self):
            print(f'attacking with power of {self.power}) 

    class Archer(User):
        def __init__(self, name, num_arrows):
            self.name = name
            self.num_arrows = num_arrows

        def attack(self):
            print(f'attacking with arrows: arrows left- {self.num_arrows}) 


    #instantiate the class

    wizard1 = Wizard('merlin', 50)
    archer1 = Archer('Robin', 100)
    wizard1.attack()
    archer1.attack()

    ```
    - Python has a tool to check if something is an instance of a class:
        - isinstance(instance, Class)
        - wizrd1 = Wizard('Merlin', 60)
        - isinstance(wizard1, Wizard) = True

    ##Everything in Python inherits from the base object class

4. Polymorphism - poly - many / morphism - form - manyforms
    - allows us to have many forms
    - redefine methods for derived classes
    - obj that gets instantiated can behave in different ways
    - mpdify classes to specific needs
    - but also DRY

    - methods belong to objects 
    - object classes can share the same method name 
    - but can act differently based on what obj calls them

    - eg in our wizard example - attack acts differently for the wizard or the archer

    def player_attack(char):
        char.attack()
    ```
    player_attack(wizard1)
    player_attack(archer1)

    ```
    gives you different results