bits = int('0101010101', 2)
print("Initial value:",bin(bits))
if (bits & (1<<1)): # if 2nd bit is 1 -> do nothing
    print("No amendmends were made")
else:   # otherwise set 2nd bit to 1
    bits = (bits ^ (1<<1))
    print("Amended 2nd bit to 1:",bin(bits))
    
