user = {"weapons": "lightsabre", "age": 38, "name": "maria"}

user.get("fav_food")
# returns None
# avoids errors
# if you want a default do this:
#     user.get['fav_food', 'tomato']
#     look for fav_food if fav_food does not exist use this default

# create a dict
# user2 = dict(key=value)

user2 = dict(name="maria")

"age" in user
# does this exist in this
"age" in user.keys()
"age" in user.values()
# what is the key what is the value
user.items()
# grab everything in the dict returns as a tuple
user.clear()
# in place removes everything
user2 = user.copy()
# create a copy for a new user
user.pop()
# remove a key, or add teh key to remove a specific one
user.popitem()
# randomly pops off something - dont use
user.update({"age", 55})
# will update the key you requested to update
# if it doesnt exist it will update and add a new key item
