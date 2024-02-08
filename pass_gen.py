# Made with ❤️ by Garry
# 07/02/2024

import random, string

class generator:
    def __init__(self):
        self.strength = 1

        self.lower_char_bank = [char for char in string.ascii_lowercase]
        self.upper_char_bank = [char for char in string.ascii_uppercase]
        self.digi_bank = [char for char in string.digits]
        self.spec_bank = [char for char in "!@#$%^&*_-"]

    def generate(self, length, strength):
        all = self.lower_char_bank + self.upper_char_bank + self.digi_bank + self.spec_bank

        strength = strength if not strength < 1 else 1

        min_length = strength * 4
        if length < min_length:
            length = min_length

        running = True
        while running:
            lower_char_count, upper_char_count, digi_count, spec_count = 0, 0, 0, 0
            password = []

            for x in range(length):
                password.append(all[random.randint(0, len(all)-1)])
            
            for char in password:
                if char in self.lower_char_bank:
                    lower_char_count +=1
                elif char in self.upper_char_bank:
                    upper_char_count +=1
                elif char in self.digi_bank:
                    digi_count +=1
                elif char in self.spec_bank:
                    spec_count +=1
                    
            if (
                lower_char_count >= strength
                and upper_char_count >= strength
                and digi_count >= strength
                and spec_count >= strength
            ):
                running = False
                    
        return "".join(password)

if __name__ == "__main__":
    try:
        app = generator()

        length = input("How many characters? ")
        length = int(length) if length else 0

        strength = input("How strong? ")
        strength = int(strength) if strength else 0

        password = app.generate(length, strength)
        pass_len = len(password)

        print("*"*pass_len)
        print("\n"+password+"\n")
        print("*"*pass_len)

    except Exception as e:
        print("error:", e)