FIRST_CHAR_CODE = ord("A")
LAST_CHAR_CODE = ord("Z")
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1


def caesar_shift(message, shift):
    # Result placeholder.
    result = ""

    # Go through each of the letters in the message.
    for char in message.upper():
        if char.isalpha():
            # Convert character to the ASCII code.
            char_code = ord(char)
            new_char_code = char_code + shift#Adding the shift value to the letter

            if new_char_code > LAST_CHAR_CODE:#to prevent non-numeric conversions
                new_char_code -= CHAR_RANGE

            if new_char_code < FIRST_CHAR_CODE:#for non-capital letters
                new_char_code += CHAR_RANGE

            new_char = chr(new_char_code)#converting ASCII to letters
            result += new_char
        else:
            result += char

    return result


user_message = input("Message to Encrypt: ")
user_shift_key = int(input("Shift Key (integer): "))
cipher_text = caesar_shift(user_message, user_shift_key)
print(f"Cipher Text: {cipher_text}")