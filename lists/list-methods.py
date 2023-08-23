#list methods are actions we can take on lists
# a method is an action we take on something

# https://www.w3schools.com/python/python_ref_list.asp

basket [1,2,3,4,5,'a']
print(len(basket))
# prints 5

# if we want to add something:
basket.append(100)

# append changes the list in place 
# what does in place mean? it means it doesnt produce a value it just appends something to the list you gave it
new_list = basket 
# will point to the list that is modified

# to add something to a specific place use insert

basket.insert(4, 500)
# inserts 100 to the 4th place of the new_list
# again it will not out put a new list it adds to the memory

basket.extend([100. 100])
# takes an iterable and can loop over 

#removing
basket.pop()
# will remove from the end
# pop will return whatever you remove

# if you add the index eg pop(0) would move from index 0

basket.remove(4)
# would remove the value that you give it
# again this works in place - DOESNT RETURN IN VALUE

# clear
basket.clear()
# removes everything in the list


#where is the item in my list?
# will return where the item is
# you can also give a parameter of where to start and end
basket.index('a',0,2)

# keyword - in

print('d' in basket)
# search for something in the list

basket.count('a')
# how many times does an item occur?

basket.sort()
# sorts the list in place
print(basket)
# will give you the sorted list

# or you can do 
print(sorted(basket))
# sorted will produce a new array and organise it

basket.copy()

basket.reverse()
# reverses the basket in place (not alphabetically but just the opposite way)
# if you want to sort and reverse do:
#     basket.sort()
#     basket.reverse()
