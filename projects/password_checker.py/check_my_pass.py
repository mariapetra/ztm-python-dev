import requests
import hashlib
import sys

# uses something called hashing
# you should never store a users password in plain text
# hasing is a one way function
# k anonymity - allows somebody to receive info about us but not know who we are
# we only give the first 5 chars of our hash password


# https://pypi.org/project/requests/
# https://passwordsgenerator.net/sha1-hash-generator/
# https://haveibeenpwned.com/Passwords


def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f"Error fetching: {res.status_code}, check api and try again"
        )
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(
                f"{password} was found {count} times.. you should probably change your password"
            )
        else:
            print(f"{password} not found carry on!")
        return "done"


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
