# 'me me me'
# each character is in a different index _LoggerConfiguration

selfish = "abcdefghijklmnop"
print(selfish[1])

# can also do start and stop and stepover
# [start:stop:stepover]
print(selfish[0:8:2])
# prints aceg

# if you want it just to start later you could do:
print(selfish[3:])

# print it backwards
print(selfish[::-1])
