# https://www.w3schools.com/python/python_ref_set.asp

my_set = {1,2,3,4,5}
your_Set = {4,5,6,7,8,9}

print(my_set.difference(your_Set))
# will return the difference in my_set from your_set

print(my_set.discard(5))
# will remove the item

print(my_set.difference_update(your_Set))
# will update by removing the differences (4,5 removed)

print(my_set.intersection(your_Set))
# will give 4,5 as they are the common things or
my_Set & your_Set

print(my_set.isdisjoint(your_set))
# do  these things have anything in common?

print(my_set.union(your_Set))
# will join the two sets and remove any duplicates
# or you can use:
print(my_set | your_Set)

my_set.issubset(your_Set)
# is my_set inside of your_Set

my_set.issuperset(your_Set)
# does yourset encompass everything in myset (does it include everything that is in it)
