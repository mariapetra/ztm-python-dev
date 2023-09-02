""""
in python we can use 'if' to see if some condition exists

"""

IS_OLD = True
IS_LICENSED = True

if IS_OLD and IS_LICENSED:
    print("you are old enough and licensed to drive")
elif IS_LICENSED:
    print("you are licensed but not old enough")
else:
    print("you cant drive")
