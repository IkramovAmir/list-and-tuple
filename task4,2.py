l = list([12, False, -5, 'HI', 90, -10, 1, True, 'HELLO', 12.32])

for i in l[:]:
    if isinstance(i, int):
        if i < 0:
            l.remove(i)
    elif isinstance(i, str):
        if i.isupper():
            l[l.index(i)] = i.lower()
print(l)