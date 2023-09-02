def say_hello(name, emoji):
    print(f'helloooooo {name} {emoji}')

# positional parameters - require to be in the proper position
say_hello('maria', ':)')

# the brackets are parameters - define
# the arguments are the value you provide to the function - call/envoke

# allows you to make functions based on the parameters/arguments - much more powerful

# key word arguments allow us to not worry about the position
# maybe bad practice as you are making the function more complicated - can also get confused with default parameters
say_hello(emoji=':)', name='Bibi')