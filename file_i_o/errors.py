try:
    with open ('test.txt', mode='r+') as myfile:
    text = myfile.write('hey its me')
    print(my_file.readlines())
except FileNotFoundError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print('IO error')
    raise err