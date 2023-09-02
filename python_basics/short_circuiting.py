#Short circuiting - looks confusing but is simple

is_friend = True
is_user = True

is_friend and is_user 

# will = True

if is_friend or is_user
    print('best friends forever')

# it does not care if one is false because either way it will print
# it performs the first true
# a bit more efficient as will stop at first true
