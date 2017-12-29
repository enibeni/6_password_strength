import string
import getpass


def check_pass_length_more_than(password_strength, password, length):
    if len(password) < length:
        return password_strength - 1
    else:
        return password_strength


def check_all_chars_are_not_the_same(password_strength, password):
    if password.count(password[0]) == len(password):
        return password_strength - 1
    else:
        return password_strength


def check_all_chars_are_not_the_same_type(password_strength, password):
    if password.isdigit() or password.isalpha():
        return password_strength - 1
    else:
        return password_strength


def check_all_chars_are_not_the_same_case(password_strength, password):
    if password.islower() or password.isupper():
        return password_strength - 1
    else:
        return password_strength


def check_years_not_in_pass(password_strength, password):
    year_from = 1901
    year_to = 2018
    if any(year for year in range(year_from, year_to) if str(year) in password):
        return password_strength - 1
    else:
        return password_strength


def check_pass_not_in_blacklist(password_strength, password, blacklist):
    if any(word for word in blacklist if word in password):
        return password_strength - 1
    else:
        return password_strength


def ckeck_pass_have_special_chars(password_strength, password):
    if not any(char in string.punctuation for char in password):
        return password_strength - 1
    else:
        return password_strength


def load_blacklist_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()
        blacklist = text.split("\n")
    return blacklist


def enter_password():
    while True:
        print("enter your password:")
        password = getpass.getpass().strip(" ")
        if password != "":
            return password
        else:
            print("password can't be empty! Try again")


if __name__ == "__main__":
    password_strength = 10

    easy_password_length = 7
    normal_password_length = 9
    hard_password_length = 10

    blacklist = load_blacklist_file("blacklist.txt")

    password = enter_password()

    password_strength = check_pass_length_more_than(
        password_strength,
        password,
        length=easy_password_length
    )
    password_strength = check_all_chars_are_not_the_same(
        password_strength,
        password
    )
    password_strength = check_all_chars_are_not_the_same_type(
        password_strength,
        password
    )
    password_strength = check_all_chars_are_not_the_same_case(
        password_strength,
        password
    )
    password_strength = check_pass_length_more_than(
        password_strength,
        password,
        length=normal_password_length
    )
    password_strength = check_years_not_in_pass(
        password_strength,
        password
    )
    password_strength = check_pass_not_in_blacklist(
        password_strength,
        password,
        blacklist
    )
    password_strength = ckeck_pass_have_special_chars(
        password_strength,
        password
    )
    password_strength = check_pass_length_more_than(
        password_strength, password,
        length=hard_password_length
    )
    print("your password strength ->> {}".format(password_strength))


