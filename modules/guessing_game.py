#generate a number 1 - 10
#get an input from user
#check input is a number 1-10
#chekc if number is the right guess
#otherwise ask again

from random import randint

answer = randint(1,10)

# how about if we want the user to guess in the terminal?
#import sys
# answer = randint(int(sys.argv[1]),int(sys.argv[2]))

while True:
    try:
        guess = int(input('guess a number 1-10:  '))
        if 0 < guess < 11:
            print('all good')
            if guess == answer:
                print('yay you did it')
                break
            break
        else:
            print('guess a number 1-10 only!:  ')
    except ValueError:
        print('please enter a number')
        continue
