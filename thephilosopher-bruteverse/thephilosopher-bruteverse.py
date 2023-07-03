#!/usr/bin/env python3

# Link: https://crackmes.one/crackme/634bdec633c5d4425e2cd8ee

# The binary itself contains only a single small function, personally got fooled by
# the crackme's rating (3.3) as this is a really easy one. The algorithm does bitwise
# XOR with 0xa3 for certain characters to reveal the flag. As the whole binary is small,
# it's relatively easy to find a bunch of undefined bytes in the middle of it. Those
# are the bytes that can be used to brute force the flag.

data = [
    0xBB,
    0x96,
    0x81,
    0x96,
    0xD3,
    0x9A,
    0x80,
    0xD3,
    0x8A,
    0x9C,
    0x86,
    0x81,
    0xD3,
    0x95,
    0x9F,
    0x92,
    0x94,
    0xD3,
    0xC9,
    0xD3,
    0xA1,
    0xC1,
    0xA5,
    0xC1,
    0xA1,
    0xC6,
    0xBA,
    0xBD,
    0xC6,
    0xAC,
    0xC7,
    0xA0,
    0xAC,
    0xA1,
    0xC7,
    0xC1,
    0xBF,
    0xBF,
    0xC4,
    0xAC,
    0xB5,
    0xC1,
    0xBD,
]

for k in range(256):
    print(f"{k}, ", end="")

    for d in data:
        print(f"{chr(d ^ k)}", end="")

    print("")

# Now it's simple to pick up the only sensible string from the output:
# k=243 (0xf3), Here is your flag : R2V2R5IN5_4S_R42LL7_F2N
