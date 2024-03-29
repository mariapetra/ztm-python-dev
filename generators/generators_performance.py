#

from time import time
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'it took {t2-t1}s')
        return result
    return wrapper

@performance
def long_time():
    print('1')
    for i in range(1000000):
        i*5
#generator

@performance
def long_time2():
    print('2')
    for i in list(range(1000000)):
        i*5
#list - stored to memory

long_time()
long_time2()

# very useful for caluclating large sets of data
# librarys often use generators instead of list because they are way faster