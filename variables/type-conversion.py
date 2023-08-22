# how do we convert data types?

print(type(int(str(100))))

# turns 200 into string and then number

name = 'Maria Claydon'
relationship_status = 'married'
current_year = 2023
birth_year = (input('what year were you born?'))
age = current_year - int(birth_year)
print(f"your age is {age}")