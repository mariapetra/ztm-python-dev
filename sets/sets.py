# data structure
# unordered collections of unique objects
my_set = {1,2,3,4,5,5}
# would only return 1 of the 5's
my_set.add(100)

how would we change a list to a set?

my_list = [1,2,3,4,5,6]
set(my_list)
# will return the list as a set removing all duplicates

# set does not import indexing
# you have to grab everything by the item

print(1 in my_set)
# you can also convert a set to a list
# you can copy your set
# you can clear your set
