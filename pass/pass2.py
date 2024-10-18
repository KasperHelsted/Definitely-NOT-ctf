def password_decoder():
    print("Enter Encoded Password (Hex):")
    pass_encoded_hex = input().strip()

    # Remove any spaces from the input
    pass_encoded_hex = pass_encoded_hex.replace(' ', '')

    # Convert hex string to bytes
    try:
        encoded_bytes = bytes.fromhex(pass_encoded_hex)
    except ValueError:
        print("Invalid hexadecimal input.")
        return

    pass_plain = ''
    j = 1

    for i in range(len(encoded_bytes)):
        char_ascii = encoded_bytes[i] - 1  # CHAR-ASCII = ord(char) - 1
        position = i + 1  # Adjust for 1-based index in COBOL

        if j == 1:
            temp_ascii = char_ascii - 16 - position
            temp_char = chr(temp_ascii + 1)
            pass_plain += temp_char
            j = 2
        elif j == 2:
            temp_ascii = char_ascii + 25 - position
            temp_char = chr(temp_ascii + 1)
            pass_plain += temp_char
            j = 3
        elif j == 3:
            temp_ascii = char_ascii - 19 - position
            temp_char = chr(temp_ascii + 1)
            pass_plain += temp_char
            j = 4
        elif j == 4:
            x = 2 * (char_ascii - 25)
            c0_a = x - 2
            temp_ascii_a = c0_a - position
            temp_char_a = chr(temp_ascii_a + 1)

            c0_b = x + 51
            temp_ascii_b = c0_b - position
            temp_char_b = chr(temp_ascii_b + 1)

            # Check if temp_ascii_a is in printable ASCII range
            if 32 <= temp_ascii_a + 1 <= 126:
                pass_plain += temp_char_a
            # Check if temp_ascii_b is in printable ASCII range
            elif 32 <= temp_ascii_b + 1 <= 126:
                pass_plain += temp_char_b
            else:
                print(f"Error in decoding at position {position}")
                return
            j = 1

    print("Decoded Password:", pass_plain)


if __name__ == "__main__":
    password_decoder()
