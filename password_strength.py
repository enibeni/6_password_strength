import string
import getpass
import datetime


def check_pass_length_more_than(password, length):
    return len(password) < length


def check_all_chars_are_not_the_same(password):
    return password.count(password[0]) == len(password)


def check_all_chars_are_not_the_same_type(password):
    return password.isdigit() or password.isalpha()


def check_all_chars_are_not_the_same_case(password):
    return password.islower() or password.isupper()


def check_years_not_in_pass(password):
    years_range = 100
    year_to = datetime.datetime.now().year
    year_from = year_to - years_range
    return any(year for year in range(year_from, year_to) if str(year) in password)


def check_pass_not_in_blacklist(password, blacklist):
    return any(word for word in blacklist if word in password)


def check_pass_not_without_special_chars(password):
    return not any(char in string.punctuation for char in password)


def load_blacklist_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()
        blacklist = text.split("\n")
    return blacklist


def enter_password():
    password = getpass.getpass("Enter your password:").strip(" ")
    if password != "":
        return password
    else:
        print("Password can't be empty! Please, try again")
        return None


if __name__ == "__main__":
    password_strength = 10

    easy_password_length = 7
    normal_password_length = 9
    hard_password_length = 10

    blacklist = load_blacklist_file("blacklist.txt")

    password = enter_password()
    if password is None:
        exit(1)

    password_strength -= (check_pass_length_more_than(
        password,
        length=easy_password_length
    ) + check_all_chars_are_not_the_same(
        password
    ) + check_all_chars_are_not_the_same_type(
        password
    ) + check_all_chars_are_not_the_same_case(
        password
    ) + check_pass_length_more_than(
        password,
        length=normal_password_length
    ) + check_years_not_in_pass(
        password
    ) + check_pass_not_in_blacklist(
        password,
        blacklist
    ) + check_pass_not_without_special_chars(
        password
    ) + check_pass_length_more_than(
        password,
        length=hard_password_length
    ))
    print("Your password strength is {}".format(password_strength))


