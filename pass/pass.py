# Python equivalent of the COBOL password encoder program

# Read the input password up to the first space
input_string = input()
passplain = input_string.split(' ')[0]
string_length = len(passplain)
passencoded = ''
J = 1

for I in range(1, string_length + 1):  # I from 1 to string_length
    TEMP_CHAR = passplain[I - 1]
    CHAR_ASCII = ord(TEMP_CHAR) - 1

    if J == 1:
        CHAR_ASCII += I
        CHAR_ASCII += 16
        J = 2
    elif J == 2:
        CHAR_ASCII += I
        CHAR_ASCII -= 25
        J = 3
    elif J == 3:
        CHAR_ASCII += I
        CHAR_ASCII += (12 * 2) + (40 // 5) - 13
        J = 4
    elif J == 4:
        CHAR_ASCII += I
        if CHAR_ASCII % 2 == 0:
            CHAR_ASCII += 2
        else:
            CHAR_ASCII -= 51
        if CHAR_ASCII % 2 == 0:
            CHAR_ASCII = (CHAR_ASCII // 2) + (3 ** 2) + (2 ** 4)
        J = 1

    CHAR_ASCII = int(CHAR_ASCII)
    passencoded += chr(CHAR_ASCII + 1)

# Convert the encoded password to hexadecimal representation
encoded_password_hex = ''.join(format(ord(c), '02x') for c in passencoded)

print("Encoded Password: " + encoded_password_hex)
