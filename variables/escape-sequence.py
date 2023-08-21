# escape sequence

from msilib.schema import tables


weather = "It's sunny"
# or
weather2 = "It'\s \"kind of\"sunny"
weather3 = "It's \n sunny"

# whatever comes after \ is a str
# \t will add a tab
# \n will add a new line
print(weather)
