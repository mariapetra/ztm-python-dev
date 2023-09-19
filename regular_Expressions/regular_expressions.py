# not unique to py
import re

pattern = re.compile("this")
string = "search inside of this text please!"

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)

print(a.span())
print(a.start())
print(a.end())
print(a.group())
# group useful with multiple searches within one line
# if none you will get an error
