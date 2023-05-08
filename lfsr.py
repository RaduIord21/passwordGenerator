from random import randint
import sys

from time import time,sleep

def xor(a, b):
    if a == b:
        return 0
    return 1


def lfsr():  # vor fi alese pozitiile 1, 2, 4, 5 si 8
    password = []
    seed = int(time() * 1000.0)
    seed_digits = [int(d) for d in str(bin(seed))[2:]]
    for each in range(16):
        password.append(seed_digits.pop())
        seed_digits.insert(0, xor(xor(xor(xor(seed_digits[1], seed_digits[2]), seed_digits[4]), seed_digits[5]), seed_digits[8]))
    return int("".join(str(x) for x in password), 2)
def shuffle(lst):
    for each in range(len(lst)):
        sleep(0.1)
        tmp = lst[lfsr() % len(lst)]
        aux = lst[each]
        lst[each] = tmp
        tmp = aux
    return lst
