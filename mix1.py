l = list([12,"salom",True, 12.12, "nima", 5, False])
new_l = []
for i in l:
    if isinstance(i, str):
        if i.islower():
            new_l.append(i.upper())
        else:
            new_l.append(i)

print(new_l)            