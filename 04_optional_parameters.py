def soma3(x = 0, y = 0, z = 0):
    res = x + y + z
    print(res)

soma3(1,2,3)
soma3(1,2) # z was omitted
soma3(1) # z, y was omitted
soma3() # z, y, x was omitted