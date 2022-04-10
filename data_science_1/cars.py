import pandas as pd

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True] #guida a destra o a sinistra
cpc = [809, 731, 588, 18, 200, 70, 45] #numero di auto ogni 1000 persone

#creo il dizionario
my_dict = {'country':names, 'drives_right':dr, 'cars_per_cap':cpc}

#creo il dataframe
cars = pd.DataFrame(my_dict)

#print("Senza etichette")
#print(cars)

#inserisco le etichette iniziali
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

#assegno agli indici del dataframe le etichette
cars.index = row_labels

#print("\nCon etichette")
print(cars)
#print(cars[['country']]) #per printare solo una colonna
#print(cars[['country', 'drives_right']]) #per printare più di una colonna
#print(cars[1:4]) #per printare un tot di righe
#print(cars.loc[['AUS']]) #loc è basato sull'etichetta, quindi prende tutti i dati che si trovano affianco ad essa
#print(cars.loc[['AUS'], ['country', 'drives_right']]) #con la virgola possiamo inserire anche quali colonne devono essere printate
#print(cars.iloc[[1,2]]) #iloc è basato sulla posizione, printa i dati in base all'indice
#print(cars.iloc[[1,2], [0,1]]) #con la virgola possiamo iserire anche quai colonne devono essere printate

