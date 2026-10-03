import random
import string

def generate_password():
    generated_password = []
    print("welcome to password generator(:")
    password_sum = int(input("enter the total number of characters in the password: "))
    letters_number = int(input("enter the number of letters in the password: "))
    numbers_number = int(input("enter the number of numbers in the password: "))
    symbols_number = int(input("enter the number of symbols in the password: "))
    
    generated_letters = random.choices(string.ascii_letters, k=letters_number)
    generated_number = random.choices(string.digits, k=numbers_number)
    generated_symbols = random.choices(string.punctuation, k=symbols_number)
    
    generated_password = generated_letters + generated_number + generated_symbols
    random.shuffle(generated_password)
    
    final_password = "".join(generated_password)
    
    if password_sum != (letters_number + numbers_number + symbols_number):
        print("invalid input! the sum of letters, numbers and characters doesn't match the password sum")
    else:
        print(f"generated password: {final_password}")

if __name__ == "__main__":
    generate_password()
