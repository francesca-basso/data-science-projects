###### PRIMO LOOP ######
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

#for i in areas :
    #print(i)

###### SECONDO LOOP (con modifiche) ######
#for index, i in enumerate(areas) :
    #print("Room " + str(index + 1) + ": " + str(i))

###### TERZO LOOP ######
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]

for x in house :
    print("The " + x[0] + " is " + str(x[1]) + " sqm")