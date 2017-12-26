import sys
import string


def get_password_strength(password):
    password_strength = 0
    blacklist = load_blacklist_file("blacklist.txt")
    if len(password) < 6:
        print("0")
        password_strength = 1
        return password_strength
    if len(password) > 6:
        print("1")
        password_strength += 1
    if len(password) > 7:
        print("2")
        password_strength += 1
    if not password.isdigit() and not password.isalpha():
        print("3")
        password_strength += 1
    if not password.islower() and not password.isupper() and not password.isdigit:
        print("4")
        password_strength += 1
    if any(char in string.punctuation for char in password):
        print("5")
        password_strength += 1
    if not any(year for year in range(1901, 2018) if str(year) in password):
        print("6")
        password_strength += 1
    if not any(word for word in blacklist if word in password):
        print("7")
        password_strength += 1
    print("result - " + str(password_strength))


def load_blacklist_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()
        blacklist = text.split("\n")
    return blacklist


if __name__ == '__main__':
    if len(sys.argv) > 1:
        get_password_strength(sys.argv[1])


