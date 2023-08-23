# list unpacking 

a,b,c = [1,2,3]

a,b,c, *other = [1,2,3,4,5,6,7,8,9]
# can unpack the list however you want

a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
# can unpack the list a, b , c, everything else, d = last item