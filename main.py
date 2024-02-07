# Made with ❤️ by Garry
# 07/02/2024

import random, string

qwerty = "qwertyuiopasdfghjklzxcvbnm"
lower_char_bank = string.ascii_lowercase
upper_char_bank = string.ascii_uppercase
digi_bank = string.digits
spec_bank = "!@#$%^&*_-"

all = lower_char_bank + upper_char_bank + digi_bank + spec_bank

chars = int(input("How many characters? "))

lower_char_count, upper_char_count, digi_count, spec_count = 0,0,0,0

while lower_char_count < 1 and upper_char_count < 1 and digi_count < 1 and spec_count < 1:
    password = []

    for x in range(chars):
        password.append(all[random.randint(0, len(all))])
    
    for char in password:
        if char in lower_char_bank:
            lower_char_count +=1
        elif char in upper_char_bank:
            upper_char_count +=1
        elif char in digi_bank:
            digi_count +=1
        elif char in spec_bank:
            spec_count +=1
            
print(password)