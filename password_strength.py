import string


def get_password_strength(password):
    password_strength = 10
    blacklist = load_blacklist_file("blacklist.txt")
    if len(password) > 6:
        if not password.count(password[0]) == len(password):
            if not password.isdigit() and not password.isalpha():
                if not password.islower() and not password.isupper():
                    if len(password) > 8:
                        if not any(year for year in range(1901, 2018) if str(year) in password):
                            if not any(word for word in blacklist if word in password):
                                if any(char in string.punctuation for char in password):
                                    if len(password) > 9:
                                        return password_strength
                                    else:
                                        return password_strength - 1
                                else:
                                    return password_strength - 2
                            else:
                                return password_strength - 3
                        else:
                            return password_strength - 4
                    else:
                        return password_strength - 5
                else:
                    return password_strength - 6
            else:
                return password_strength - 7
        else:
            return password_strength - 8
    else:
        return password_strength - 9


def load_blacklist_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()
        blacklist = text.split("\n")
    return blacklist


if __name__ == '__main__':
    print("enter your password:")
    password = input().strip(" ")
    print("your password strength form 1 to 10 ->> " + str(get_password_strength(password)))


