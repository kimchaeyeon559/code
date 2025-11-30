x = int(input())

line = 1
sum = 0

while sum + line < x:
    sum += line
    line += 1

pos = x - sum

if line % 2 == 0:
    numerator = pos
    denominator = line - pos + 1
else:
    numerator = line - pos + 1
    denominator = pos

print(numerator, "/", denominator)