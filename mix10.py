l = [12, False, 54.3, "salom", 43, True, "bestYear", 32, 54, False, 43.2, "new"]

digit = []

for i in l:
    if isinstance(i, (int, float)):
        digit.append(i)

digit.sort()

print(digit[len(digit) - 3:])