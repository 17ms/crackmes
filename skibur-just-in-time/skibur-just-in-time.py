#!/usr/bin/env python3

# Link: https://crackmes.one/crackme/63c4ee1a33c5d43ab4ecf49a

# Conditions that must be fulfilled for the key to be valid:
# key[0] == '%'
# key[1] << t == 200
# key[2] << t == 212
# key[3] == 'k'
# key[4] << t == 80
# key[5] & 1073741823 == 57
# key[6] == '^'
# key[7] << t == 246
# key[8] & 1073741823 == 46
# key[9] == 'f'
# key[10] << t == 128
# key[11] & 1073741823 == 49
# key[12] == 'F'
# key[13] << t == 104
# (t = (localtime() % 10) % 3) => t either 0, 1, or 2

# After these conditions are met the printable string (either "Incorrect password." or
# "Correct password. Congratulation!") is decoded by shifting each of the string's
# character's value to the right by one and subtracting 5 from that.


from string import ascii_letters, digits, punctuation
import itertools

key = ["%", "", "", "k", "", "", "^", "", "", "f", "", "", "F", ""]

for c in itertools.chain(*[ascii_letters, digits, punctuation]):
    shift = ord(c) << 1

    match shift:
        case 200:
            key[1] = c
        case 212:
            key[2] = c
        case 80:
            key[4] = c
        case 246:
            key[7] = c
        case 128:
            key[10] = c
        case 104:
            key[13] = c

    band = ord(c) & 0x3FFFFFFF

    match band:
        case 57:
            key[5] = c
        case 46:
            key[8] = c
        case 49:
            key[11] = c

print(f"{''.join(key)}")
