zip = './file/x-the-unknown.zip'
zip2 = './file/x-the-unknown2.zip'

with open(zip, 'rb') as f:
    data = f.read()
with open(zip2, 'wb') as f:
    f.write(data)
