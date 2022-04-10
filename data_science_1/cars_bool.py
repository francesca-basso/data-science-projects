import pandas as pd
import numpy as np

#csv di merda
cars = pd.read_csv(r"C:\Users\franc\Documents\Progetti personali\progetti in python\cars.csv", index_col=0)

#print(cars)

#assegno a sel tutti i bool di drives_right, vengono printati solo i True
sel = cars.loc[:, 'drives_right']

#print(cars[sel])

#voglio solo i paesi con una quantità di macchine per capite maggiore di 500
cpc = cars.loc[:, 'cars_per_cap']
many_cars = cpc > 500
cars_maniac = cars[many_cars]
#print(cars_maniac)

#voglio solo i paesi con una quantità di macchine per capite maggiore di 100 e minore di 500
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]
print(medium)