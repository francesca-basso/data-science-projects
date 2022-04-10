import pandas as pd

netflix_data = pd.read_csv(r"C:\Users\franc\Documents\Progetti personali\progetti in python\data_science_2\netflix_data.csv")

#vengono sortati in valore ascendente
netflix_dur = netflix_data.sort_values("duration")
print(netflix_dur.head())

#vengono sortati in valore discendente
netflix_dur_2 = netflix_data.sort_values("duration", ascending=False)
print(netflix_dur_2.head())

#vengono presi in conderazione due valori, uno sortato in modo ascendente e l'altro in modo discendente
netflix_tit_dur = netflix_data.sort_values(["title", "duration"], ascending=[True, False])
print(netflix_tit_dur.head())