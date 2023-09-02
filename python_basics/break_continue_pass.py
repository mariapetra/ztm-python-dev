# break breaks out of the current and continuing loop

# however with a continue we are saying whatever happens continue to the top 

my_list = [1,2,3]
for item in my_list:
    continue
    print(item)

# the print statment in the above will never run as it will continue to the top line 5-7 continuously
# pass is not very useful it does nothing - it just passes to the next line - very rare you will see it in your code
# you may use it as a placeholder - line of code that means nothing that we can pass through