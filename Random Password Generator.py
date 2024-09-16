import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):

    characters = ''
    if use_letters:
        characters += string.ascii_letters  # Upper and lowercase letters
    if use_numbers:
        characters += string.digits  # Numbers 0-9
    if use_symbols:
        characters += string.punctuation  # Special characters


    if not characters:
        print("You must select at least one character type (letters, numbers, symbols)!")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Password length should be greater than zero.")
            exit()
    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")
        exit()
        
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

 
    password = generate_password(length, use_letters, use_numbers, use_symbols)

    if password:
        print(f"Generated Password: {password}")
