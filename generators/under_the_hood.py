def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterartor))
        except StopIteration:
            break

special_for([1,2,3])
# iter will allow us to use the next function


class MyGen():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if  MyGen.current < self.last:
            num = MyGen.current
            MyGen.cuurent += 1
            return num
        raise StopIteration

gen = MyGen(0,100)
for i in gen:
    print(i)