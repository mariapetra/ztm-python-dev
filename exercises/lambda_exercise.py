#Square

my_list = [1,2,3]

print(list(map(lambda item: item*item, my_list)))

#List Sorting - by second item in Tuple

my_list2 = [(0,2),(4,3),(9,9),(10,-1)]

my_list2.sort(key=lambda a:a[1])