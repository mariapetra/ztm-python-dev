# in python we can use 'if' to see if some condition exists
is_old = True
is_licenced = True

if is_old and is_licensed: 
    print('you are old enough and licensed to drive')
elif is_licensed:
    print('you are licensed but not old enough')
else:
    print('you cant drive')