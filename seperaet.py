s = input()

up, low = [], []

for char in s:
    if char.isupper():
        up.append(char)

    else:
        low.append(char)

print("".join(up))
print("".join(low))
