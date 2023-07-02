#!/usr/bin/env python3

# Link: https://crackmes.one/crackme/60c24a7133c5d410b8842d3c

# The algorithm simply checks pw[4]=='@' && pw[6]=='-' && pw[9]=='l' && pw[15]=='?'.

import random
import string

for i in range(1, 51):
    pw = random.choices(string.ascii_letters + string.digits, k=16)
    pw[4] = "@"
    pw[6] = "-"
    pw[9] = "l"
    pw[15] = "?"

    print(f"{i}: {''.join(pw)}")
