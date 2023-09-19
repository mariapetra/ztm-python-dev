import re

# see regex options here: # https://www.w3schools.com/python/python_regex.asp
# https://regex101.com/

pattern = re.compile(r"([a-zA-Z]).([a])")
# r = raw string
# . = anything

# https://regexone.com/

# how is this appled to real life scenarios?
# imagine you have a startup and want to collect emails from interested customers
# this should have a correct email otherwise ask them to try again

pattern_email = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b")

a = pattern_email.search(string)
print(a)

password = "test"

pattern_pw = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")
check = pattern_pw.fullmatch(password)