#MRO - method resolution order - a rule that python follows to dtermine when you run a method which one should you run
# What is first in line?
# you probably will never use this or be tested on it

# Check this by doing:
# https://replit.com/@aneagoie/MRO
# http://www.srikanthtechnologies.com/blog/python/mro.aspx

print(D.mro())

class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, G):
    pass



#     A
#    / \
#   /   \
#  B     C
#  \     /
#   \   /
#     D


