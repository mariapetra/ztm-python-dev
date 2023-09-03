# Create 2 inputs - username and password
# Print the password secret and password length
# convert password to ******* (print * x password(len))
# Should have a greeting

username = input("Enter your username: ")
password = input("Enter your password: ")
pw_length = int(len(password))
scrambled_pw = "*" * pw_length

print(
    f"Hi {username.capitalize()}, your password, {scrambled_pw} is {pw_length} characters long"
)
