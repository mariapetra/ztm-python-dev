WHat is it?

seperation of concerns - each part concerns itself with one things its good at
packaging our code into seperate chunks so everything is organised
seperate data and functions
data = interacted and acted upon
functional - emphasis on simplicity whwre data and functions are concerned

making our code clean and understandable
easy to extend
easy to maintain
memory efficient
DRY


Pure function - a simple function
Something will happen to an input - everytime it says the same thing
input should = output
should not have any side effects
should not interact with the outside workd

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return (new_list)

multiple_by2([1,2,3])
- pure function

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return print(new_list)

multiple_by2([1,2,3])
- not pure function as print interacts with the outside world

new_list = []
def multiply_by2(li):
    for item in li:
        new_list.append(item*2)
    return print(new_list)

multiple_by2([1,2,3])
- not pure function as print interacts with the outside world - has side effects
- someone could change the new_list in the outside world