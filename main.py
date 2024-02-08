# Made with ❤️ by Garry
# 07/02/2024

import random, string

lower_char_bank = string.ascii_lowercase
upper_char_bank = string.ascii_uppercase
digi_bank = string.digits
spec_bank = "!@#$%^&*_-"

all = lower_char_bank + upper_char_bank + digi_bank + spec_bank

chars = int(input("How many characters? "))

if chars < 8:
    chars = 8

lower_char_count, upper_char_count, digi_count, spec_count = 0,0,0,0

running = True
while running:
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
    
    if lower_char_count > 1 and upper_char_count > 1 and digi_count > 1 and spec_count > 1:
        running = False
            
password = "".join(password)
pass_len = len(password)

print("*"*pass_len)
print("\n"+password+"\n")
print("*"*pass_len)