# use a variable outside of the scope of my function
# you can use a variable from the parent scope as long as it is not a global variable
# too complex - dont use if you can avoid


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "non local"
        print("inner", x)

    inner()
    print("outer", x)


outer()
