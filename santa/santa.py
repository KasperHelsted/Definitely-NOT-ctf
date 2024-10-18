import binascii

# Open the binary file
with open('./SantasTinyHelper', 'rb') as binary_file:
    # Read the binary data
    binary_data = binary_file.read()

    # Decode the binary data to text
    # You can change 'utf-8' to another encoding if necessary
    text_data = binascii.hexlify(binary_data).decode('utf-8')

    # Print the text data
    print(text_data)