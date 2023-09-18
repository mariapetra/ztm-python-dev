# file - input output
# maybe you want to speak to another website or something else on your desktop

# input something from the outside world 
# input image / output compressed file 

# python has a built in function:

myfile = open('test.txt')
myfile.read()
# you can read your file in the terminal
# - you can only read the file once

myfile.seek(0)
# moves your cursor to wherever you want - 0 = starts at the beginning
myfile.readline()
# moves cursor to a line
myfile.readlines()
# list that reads the entire file

# you also have to manually close the file:
myfile.close()