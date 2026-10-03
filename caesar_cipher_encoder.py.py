import string

uppercase_dictionary = string.ascii_uppercase
lowercase_dictionary = string.ascii_lowercase
encrypted_message = ""
print(f"Welcome to caesar chiper encoder(:\n")

message_to_encryption = input("enter a message: ")
shift_number = input("enter a shift: ")

for letter in message_to_encryption:
    if letter in uppercase_dictionary:
        letter_position = uppercase_dictionary.index(letter)
        letter_new_position = (letter_position + int(shift_number)) % 26
        encrypted_message += uppercase_dictionary[letter_new_position]
    elif letter in lowercase_dictionary:
        letter_position = lowercase_dictionary.index(letter)
        letter_new_position = (letter_position + int(shift_number)) % 26
        encrypted_message += lowercase_dictionary[letter_new_position]
    else:
        encrypted_message += letter

print(encrypted_message)
