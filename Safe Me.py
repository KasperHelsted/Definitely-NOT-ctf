a = [x for x in range(1000, 9999) if '0' not in str(x)]
b = [x for x in range(10000, 99999) if '0' not in str(x)]

for a1 in a:
    a1_str = str(a1)
    if len(set(a1_str)) != len(a1_str):
        continue

    for b1 in b:
        b1_str = str(b1)

        if len(set(b1_str)) != len(b1_str):
            continue

        data = [x for x in (a1_str + b1_str)]
        if len(set(data)) != 9:
            continue

        if a1 * 3 == b1:
            print(a1, b1)
