some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

# find-duplicate
duplicates = []

for letter in some_list:
    if some_list.count(letter) > 1:
        if letter not in duplicates:
            duplicates.append(letter)

print(duplicates)


another_list = ["z", "ff", "f", "z", "z"]

morethan1 = []

for char in another_list:
    if another_list.count(char) > 2:
        morethan1.append(char)

print(morethan1)
