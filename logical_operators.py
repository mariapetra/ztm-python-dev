# very useful with conditional logic
# allows us to perform logic between two things

and
or
>
<
==
>=
<=
!=
not
# not means the opposite eg not True = false
# not is a keyword and also a function: print(not(True))

is_magician = False
is_expert = True

#check if magician AND expert - if True print you are a master magician

if is_magician and is_expert:
    print('you are a master magician')
elif is_magician and not is_expert:
    print('at least youre getting there')
else:
    print('you need magic powers')
