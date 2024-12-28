l = "Python programming is amazing!"
a = list(l)
p = 0
new_str = []
for i in a:
    if p == 0:
        new_str = i
    elif a[p] == " ":
        new_str += a[p + 1]
    
    p += 1    

print(new_str)