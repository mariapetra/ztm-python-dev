#Ternary operator is a shortcut  -makes your code alittle bit cleaner
# can also be called a condition expression
# an expression evaluates to a value

condition_if_true if condition else condition_if_else

# what does this mean?
# starts at if condition - if true moves to the left - otherwise moves to the right

is_friend = True 
can_message = 'message allowed' if is_friend else 'not allowed to message'

print(can_message)