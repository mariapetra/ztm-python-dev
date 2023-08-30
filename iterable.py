# iterable is an action 

# can be iterated:

#     list, dictionary, tuple, set, string

# iterated = one by one check each item in the collection

# example

user {
    name: 'golem'
    'age': 5006,
    'can_swim': False,
}

for item in user:
    print(item)

# will prnt keys

for item in user.items()
    print(item)

# this will print the keys and values as a tuple

for item in user.values()
    print(item)
# this will print the values

for item in user.keys()
    print(item)
# this will print the keys

# these allow us to iterate over dictionaries

for key, value in user.items()
    print(item)

# will print them seperately not as a tuple