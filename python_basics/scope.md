# what is scope?

# Scope = what variables do i have access to?

you only create a new scope when you define a function like a new world - anything indented is its own world

1. Start with local
2. Parent local
3. Global
4. Built in python functions

Global keywords:

you can use 'global' to access a variable outside of a function

total = 0

def count():
    global total
    total += 1
    return total

not a good way to do this too messy for big files


why do we need scope?

saves memory

once a function is finished garbage collector says hey we are done with this - lets collect the garbage and throw it out.
