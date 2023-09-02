:=

# this is a new feature - walrus operator
assigns values to variables as part of a larger expression

a = 'helooooo'

if ((n :=len(a)) > 10):
    print(f"too lon {n} elements")

