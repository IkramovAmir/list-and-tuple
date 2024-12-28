l = [12, True, "whassup", 34.12, False, 56, "calm", 43.90, "happy", 1]

new_l = []
new_l += l[::3]

t = tuple(new_l)

print(f"Index of 1 is {t.index(1)}")
