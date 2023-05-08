from lfsr import lfsr, shuffle
from time import sleep

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['!', '"', '#', '$', '%', '&', '\\', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=',
                      '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']

all_chars = letters + numbers + special_characters
no_letters = len(letters)
no_numbers = len(numbers)
no_special_characters = len(special_characters)


def main():
    password = []
    result = ""
    while True:
        print("Input parameters")
        min_letters = int(input("Least amount of letters: "))
        max_letters = int(input("Most amount of letters: "))
        min_numbers = int(input("Least amount of numbers: "))
        max_numbers = int(input("Most amount of numbers: "))
        min_specials = int(input("Least amount of specials: "))
        max_specials = int(input("Most amount of specials: "))
        password_length = int(input("Password Length : "))
        if min_specials + min_numbers + min_letters < password_length:
            break
        if max_specials + max_numbers + max_letters > password_length:
            break
        if min_letters < max_letters:
            break
        if min_numbers < max_numbers:
            break
        if min_specials < max_specials:
            break
        print("Invalid input !!!")
    for each in range(min_letters + 1):
        sleep(0.1)
        password.append(letters[lfsr() % no_letters])
    for each in range(min_numbers):
        sleep(0.1)
        password.append(numbers[lfsr() % no_numbers])
    for each in range(min_specials):
        sleep(0.1)
        password.append(special_characters[lfsr() % no_special_characters])
    temp_len = len(password)
    for each in range(password_length - temp_len):
        sleep(0.1)
        password.append(all_chars[lfsr() % len(all_chars)])
    for each in password:
        result += each
    return result

print(main())
