bits = int('0101010111', 2)
print("Initial value:",bin(bits))
if (bits & (1<<1)) and (bits & (1<<2)): # if 2nd and 3rd bits are 1 -> reset 2nd and 3rd bits to 0
    bits = (bits ^ (1<<1))
    bits = (bits ^ (1<<2))
    print("2nd and 3rd bits were reset to 0:",bin(bits))
else:  # otherwise do nothing
    print("No amendmends were made")
