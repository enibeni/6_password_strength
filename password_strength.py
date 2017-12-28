import string


def check_pass_length_more_than(password, required_length):
    if len(password) < required_length:
        global password_strength
        password_strength -= 1


def check_all_chars_are_not_the_same(password):
    if password.count(password[0]) == len(password):
        global password_strength
        password_strength -= 1


def check_all_chars_are_not_the_same_type(password):
    if password.isdigit() or password.isalpha():
        global password_strength
        password_strength -= 1


def check_all_chars_are_not_the_same_case(password):
    if password.islower() or password.isupper():
        global password_strength
        password_strength -= 1


def check_years_not_in_pass(password):
    if any(year for year in range(1901, 2018) if str(year) in password):
        global password_strength
        password_strength -= 1


def check_pass_not_in_blacklist(password, blacklist):
    if any(word for word in blacklist if word in password):
        global password_strength
        password_strength -= 1


def ckeck_pass_have_special_chars(password):
    if not any(char in string.punctuation for char in password):
        global password_strength
        password_strength -= 1


def load_blacklist_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()
        blacklist = text.split("\n")
    return blacklist


if __name__ == "__main__":
    password_strength = 10
    blacklist = load_blacklist_file("blacklist.txt")

    print("enter your password:")
    password = input().strip(" ")

    check_pass_length_more_than(password, 7)
    check_all_chars_are_not_the_same(password)
    check_all_chars_are_not_the_same_type(password)
    check_all_chars_are_not_the_same_case(password)
    check_pass_length_more_than(password, 9)
    check_years_not_in_pass(password)
    check_pass_not_in_blacklist(password, blacklist)
    ckeck_pass_have_special_chars(password)
    check_pass_length_more_than(password, 10)
    print("your password strength ->> {}".format(password_strength))


