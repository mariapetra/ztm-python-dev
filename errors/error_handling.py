while True:
    try:
        age = int(input('What is your age? '))
        print(age)
    except:
        print('please enter a number')
    else:
        print('thank you')
    break

# trys the first thing, except if it doesnt work

# or you can do this base on the type of error:

while True:
    try:
        age = int(input('What is your age? '))
        10/age
    except ValueError:
        print('please enter a number')
    except ValueError:
        print('!!!!!')
    except ZeroDivisionError:
        print('please enter a number higher than 0')
    else:
        print('thank you')
    break

# trys the first thing, except if it doesnt work

def sun(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'please enter numbers {err}')

print(sum(2,2))

def sun(num1, num2):
    try:
        return num1/num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)

print(sum(2,2))

# what about if we want to stop our program?

raise ValueError
raise Exception

# errors are unavoidable - your job is to participate and handle them in your program
