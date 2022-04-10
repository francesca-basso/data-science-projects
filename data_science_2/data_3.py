import pandas as pd

netflix_data = pd.read_csv(r"C:\Users\franc\Documents\Progetti personali\progetti in python\data_science_2\netflix_data.csv")

#prendo solo una colonna
genre = netflix_data["genre"]
#print(genre.head())

#prendo più di una colonna
genre_release = netflix_data[["genre", "release_year"]]
#print(genre_release.head())

#inserisco una condizione e stampo solo i valori per cui è vera
duration = netflix_data[netflix_data["duration"] > 90]
#print(duration)

#un'altra condizione
type_film = netflix_data[netflix_data["type"] == "TV Show"]
#print(type_film)

#più condizioni insieme
dur_and_type = netflix_data[(netflix_data["duration"] > 3) & (netflix_data["type"] == "TV Show")]
#print(dur_and_type)

#solo una delle due può verificarsi
dur_and_type = netflix_data[(netflix_data["duration"] > 130 ) | (netflix_data["type"] == "TV Show")]
print(dur_and_type)