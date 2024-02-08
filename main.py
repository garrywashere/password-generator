# Made with ❤️ by Garry
# 07/02/2024

import random, string

STRENGTH = 4

lower_char_bank = [char for char in string.ascii_lowercase]
upper_char_bank = [char for char in string.ascii_uppercase]
digi_bank = [char for char in string.digits]
spec_bank = [char for char in "!@#$%^&*_-"]

all = lower_char_bank + upper_char_bank + digi_bank + spec_bank

try:
    chars = int(input("How many characters? "))
except ValueError:
    chars = 0

min_length = STRENGTH * 4
if chars < min_length:
    chars = min_length

running = True
while running:
    lower_char_count, upper_char_count, digi_count, spec_count = 0, 0, 0, 0
    password = []

    for x in range(chars):
        password.append(all[random.randint(0, len(all)-1)])
    
    for char in password:
        if char in lower_char_bank:
            lower_char_count +=1
        elif char in upper_char_bank:
            upper_char_count +=1
        elif char in digi_bank:
            digi_count +=1
        elif char in spec_bank:
            spec_count +=1
    
    if lower_char_count >= STRENGTH and upper_char_count >= STRENGTH and digi_count >= STRENGTH and spec_count >= STRENGTH:
        running = False
            
password = "".join(password)
pass_len = len(password)

print("*"*pass_len)
print("\n"+password+"\n")
print("*"*pass_len)