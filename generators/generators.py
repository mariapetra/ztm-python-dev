# very important key term
# allow us to generate a sequence of values over long_time

# a special type of thing in python - yield
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

# iterable - an object you can loop through
# under the hood it has the dunder method

# to iterate is the act of taking an item from an iterable doing something with it and going to the next one

# generators are iterable
# but not everything that is iterable is a generator

# a generator is a subset of iterable

def generator_function(num):
    for i in range(num)
        yield i

print(generator_function(10000))

# you yield instead of returning
# what does yield do?
# pauses the function and comes back to it when we do something to it- give i and when you tell me to keep going i will keep going

for item in generator_function(1000):
    print(item)

# this will print the numbers one by one

def generator_function2(num):
    for i in range(num)
        yield i*2

# g = generator_function2(100)

print(g)
# will get a generator object
next(g)
# will print 0
next(g)
# will print 4

# yield pauses the function and comes back to it when next is called
# if you were to use next after the range has expired eg for a range of 10 you call it 11 times 
# so you exceed the number of items you will get a StopIteration error