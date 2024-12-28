t = (12, 1, 43, 54, 32,64,90)

i = ""
o = 0 
for a in t:
    if o == 2 or o == 5:
        i += str(a)
    o += 1
    
print(i)