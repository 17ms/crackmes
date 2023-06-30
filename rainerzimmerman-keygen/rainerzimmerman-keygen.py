#!/usr/bin/env python3

# Link: https://crackmes.one/crackme/6403ac2a33c5d447bc76179f

# Conditions that must be fulfilled for the key to be valid:
# 1. len(key) == 13 && key[3] == "-"
# (2. sum1 = sum(key[0:3])))
# 3. (key[0] ^ sum1 % 3) == sum(key[4:7])
# 4. (key[1] ^ sum1 % 3) == sum(key[7:10])
# 5. (key[2] ^ sum1 % 3) == sum(key[10:13])

import random


def complete(base):
    s = ["", "", ""]
    base_sum = sum(base)

    for i in range(3):
        c = base[i] ^ base_sum % 3
        s[i] = "".join(str(n) for n in find_sum(c))

    return f"{''.join(str(n) for n in base)}-{s[0]}{s[1]}{s[2]}"


def find_sum(total):
    while True:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        z = random.randint(0, 9)

        if x + y + z == total:
            break

    return x, y, z


while True:
    base = [random.randint(0, 9) for _ in range(3)]
    print(complete(base))
