with open('adam2', 'rb') as f:
    testpem = f.read()  # binary data from testpem.pem

with open('adam', 'rb') as f:
    pem = f.read()  # binary data from testpem.pem

chunks = []
i = 0
while i < len(testpem):
    if testpem[i] == 0x02:
        hl = 0
        length = 0
        if (testpem[i + 1] & 0x80) > 0:
            hl = testpem[i + 1] & 0x3F
            length = int.from_bytes(testpem[i + 2:i + hl + 2], byteorder='big')
        else:
            length = testpem[i + 1] & 0x3F
        chunks.append((i + 2 + hl, i + 2 + hl + length))
        print(testpem[i + 2 + hl:i + 2 + hl + length].hex())
        print()
        i += hl + length + 2
    else:
        i += 1

print(chunks)
