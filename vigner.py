def evaluate_key(short_key, us_ms):
    # creating key with same length as message
    long_key = ''
    short_key = short_key.replace(" ", "")
    i = 0
    for char in us_ms:
        if char == ' ':
            long_key += ' '
        elif char.isalpha():
            long_key += short_key[i]
            i += 1
            if i == len(short_key):
                i = 0
        else:
            long_key += char
    return long_key


def encrypt(mess, full_key):
    # encrypting or decrypting message,
    code_mess = ''
    i = 0
    for char in mess:
        if char == ' ':
            code_mess += ' '
        elif char.isalpha():
            numeric_l = ord(char)
            numeric_k = ord(full_key[i])
            ascii_cod_m = numeric_l + (numeric_k - 65)
            if ascii_cod_m > 90:
                ascii_cod_m = ascii_cod_m - 26
            char_cod_m = chr(ascii_cod_m)
            code_mess += char_cod_m
        else:
            code_mess += char
        i += 1
    return code_mess


def decode(mess, full_key):
    decode_mess = ''
    i = 0
    for char in mess:
        if char.isalpha():
            numeric_l = ord(char)
            numeric_k = ord(full_key[i])
            ascii_cod_m = numeric_l - (numeric_k - 65)
            if ascii_cod_m < 65:
                ascii_cod_m = ascii_cod_m + 26
            char_cod_m = chr(ascii_cod_m)
            decode_mess += char_cod_m

        else:
            decode_mess += char
        i += 1
    return decode_mess
while True:
    print("1. Coding message\n2. Decoding message\n3.Quit")
    choose = int(input())
    try:
        if choose == 1:
            user_message = input("Write message to code:\t")
            # only letters can be use in key_code
            key_code = input("Write key:\t")
            if not key_code.isalpha:
                print("only char can by in key")
                continue
            prop_key = evaluate_key(key_code.upper(), user_message)
            print(f"Full key: {prop_key}")
            ready_message = encrypt(user_message.upper(), prop_key)
            print(f"Your code message {ready_message}")
        elif choose == 2:
            user_message = input("Write message to decode:\t")
            key_code = input("Write char key:\t")
            prop_key = evaluate_key(key_code.upper(), user_message)
            print(f"Full key: {prop_key}")
            ready_message = decode(user_message.upper(), prop_key)
            print(f"Your decode message {ready_message}")
        elif choose == 3:
            break
    except ValueError:
        print("Input must be an integer")
