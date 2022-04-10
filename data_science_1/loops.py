import pandas as pd

cars = pd.read_csv(r"C:\Users\franc\Documents\Progetti personali\progetti in python\cars.csv", index_col=0)

#for lab, row in cars.iterrows() :
    #print(lab + " : " + str(row['cars_per_cap']))

#crea una nuova colonna con le caratteristiche designate
#for lab, row in cars.iterrows() :
    #cars.loc[lab, "COUNTRY"] = str.upper(row['country'])

#usiamo .apply invece del for
cars["COUNTRY"] = cars['country'].apply(str.upper)

print(cars)