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
    finally:
        print('ok, i am finally done')

# finally runs regardless of anything previously
# it is good for our records
