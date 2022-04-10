####### PRIMO LOOP #######
x = 1

while x < 4 :
    #print(x)
    x = x + 1

####### SECONDO LOOP #######
offset = 8

while offset != 0 :
    #print("correcting...")
    offset = offset - 1
    #print(offset)

####### TERZO LOOP #######
offset = -6

while offset != 0 :
    print("correcting...")
    if offset > 0 :
        offset = offset - 1
    else :
        offset = offset + 1
    print(offset)