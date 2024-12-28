l = [("salom", 2, 2.12, True),("whassup", 2, 2.12, 2),("alright", True, "Max", 12)]

temp = list(l[0])
temp[2] = "changed"
l[0] = tuple(temp)
print(l[0][2])

"I opened list '[] and created a few tuples '()' that includes 3 values"
"Tuple can not be changed directly cause tuple is immutable that is why we assigned it to list to change value than assigend back to tuple"