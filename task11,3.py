t = (12,32,43,65,23,12,43,12, 4, 4, 4,4,4)

max_num = 1

for i in t:
    n = t.count(i)
    
    if n > max_num:
        max_num = n
        maximum = i


print(f"{maximum} is used {max_num} times")

      
    
        
        