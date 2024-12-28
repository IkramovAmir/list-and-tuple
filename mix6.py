l = list([(12, "whassup", 54.12, False), (5, "calm", True, 12.05), ("nima gap", 54, 54.90, False)])
a = 0
new_l = []

for i in l:
    length = len(l[a]) - 1
    
    new_l.append(l[a][length])
    a += 1
    
print(tuple(new_l))