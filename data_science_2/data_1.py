import pandas as pd

netflix_data = pd.read_csv(r"C:\Users\franc\Documents\Progetti personali\Progetti_in_Python\data_science_2\netflix_data.csv")

#printa solo le prime righe
print(netflix_data.head())

#da informazioni sul dataframe
print(netflix_data.info())

#ci dice il nunero di righe e di colonne
print(netflix_data.shape)

#ci da alcune statistiche per ogni colonna
print(netflix_data.describe())

#un array NumPy di valori a due dimensioni 
print(netflix_data.values)

#printa i nomi delle colonne
print(netflix_data.columns)

#printa il numero di righe
print(netflix_data.index)