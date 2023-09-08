# - Comprehensions - key term 

# list / set / dictionary 
# Comprehensions

# we can use them with these three data types
# quick way to create without looping

my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

# Becomes:

# param can be a variable/parameter name it wat you want eg char for char in 'hello'
my_list2 = [param for param in iterable]
hello = [char for char in 'hello']

my_numbers = [1,2,3,4,5,6,7,8]
my_list_num = [num for num in range(0,100)]
my_list3 = [num*2 for num in range(0,100)]
my_list3 = [num**2 for num in range(0,100) if num % 2 ==0]

print(my_list_num)