l = list(["hey", "how", "why", "where", "when", "which", "who", "what", "now", "whenever", 1, 3, 15, False, 21.13])
length = len(l) - 3
a = list(l[0:2] + l[length:])
a.reverse()
print(a)
