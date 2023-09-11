# very important key term
# allow us to generate a sequence of values over long_time



# a special type of thing in python
# a special keyword that can pause and resume functions

# eg 
range(100)
list(range(100))

# list creates a giant list of items in our comps memory
# range = 1 x 1

def make_list(num):
    result = []
    for i in range(n):
        result.append(i*2)
    return result

my_list = make_list(100)
print(my_list)

# my_list pointing to a location in memory - is taking up space
# range is a generator and is NOT being held in memory
# generator is more efficient - generate 1 at a time with no space in memory