with open ('test.txt', mode='r+') as myfile:
    text = myfile.write('hey its me')
    print(my_file.readlines())

# mode='r+'
# allows you to read and write to a file
#remember the cursor goes to zero so if you write more than once it will rewrite your previous line
#  so you can use append mode='a', write = mode='w', if you do read and write mode=r+ it sets the cursor 
# to 0. If you do w it will replace what you had written beore
