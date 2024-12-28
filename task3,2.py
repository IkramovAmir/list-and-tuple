t = (2,3,8)

x = list(t)
x [0] = 'haaaaaaa'
x[1] = True
x[2] = 21.23

t = tuple(x)
print(t)
print(type(t))

"as before said we can't directly change value of tuple so firt we assigned it to list to change value then assigned back to tuple"