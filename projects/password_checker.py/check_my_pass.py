import requests

url = "https://api.pwnedpasswords.com/range/" + "CBFDA"
res = requests.get(url)
print(res)

# uses something called hashing
# you should never store a users password in plain text
# hasing is a one way function
# k anonymity - allows somebody to receive info about us but not know who we are
# we only give the first 5 chars of our hash password


# https://pypi.org/project/requests/
# https://passwordsgenerator.net/sha1-hash-generator/
# https://haveibeenpwned.com/Passwords
