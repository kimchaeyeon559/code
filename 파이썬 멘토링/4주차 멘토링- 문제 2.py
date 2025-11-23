e = input()

result = ""

for ch in e:
    if 'a' <= ch <= 'z':
        new = chr(ord(ch) - 32)
        result += new

    elif 'A' <= ch <= 'Z':
        new = chr(ord(ch) + 32)
        result += new

    else:
        result += ch

print(result)