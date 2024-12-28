t = list([(5,23,14),(2, 23, 12),(4, 90, 15), (10, 70, 45), (23, 89, 34)])

j = 0
length = len(t)
search_num = 23 # if we want, we can make it input() by user
r = range(length)
count = 0

for i in r:
    if search_num in t[j]:
        count += 1
    j += 1
if count > 0:
    print(f"{search_num} is iterated {count} times")
else:
    print("There is no such kinda number!!")
    