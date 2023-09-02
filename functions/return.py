def sum(num1, num2):
    return num1 + num2

print(sum(4,5))

# a function either modifies something in our program or returns something

# good practice:

# a function should do one thing really well
# and usually a function should return something

# you can also nest functions but this would not be easy to read and shouldnt be used

def sum(num1, num2):
    def func_2(num1, num2):
        return num1 + num2
    return func_2(num1, num2)

total = sum(10,20)
print(total)

# prints 30

# Also should note return will exit the code - it will end at return