# Simple Password Generator
Just a simple password generator, written in Python 🐍.

## Why?
I was bored.

## Overview
This Python script provides a simple password generator that allows users to specify the desired length and strength of the generated password. The generator ensures a mix of lowercase letters, uppercase letters, digits, and special characters, meeting the specified strength criteria.

## Features
- Generates random passwords based on user-defined length and strength.
- Incorporates a mix of lowercase letters, uppercase letters, digits, and special characters for enhanced security.

## Usage
1. Clone the repository:

   ```bash
   git clone https://github.com/garrywashere/password-generator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd password-generator
   ```

3. Import the script in your program:

   ```python
   from password_generator import Generator
   gen = Generator()

   new_password = gen.generate(8, 1)
   ```

5. The generated password will be returned.
   - The `length` parameter determines the total number of characters in the password (minimum `strength * 4`)
   - The `strength` parameter determines the minimum number of each type of character included in the password. Example:
   - ```python
      gen.generate(4, 1)
      # At least one of each type of character is used
      '8-vR'
      ```
   - ```python
      gen.generate(8, 2)
      # At least two of each type of character are used
      'g_9z2XU^'
      ```