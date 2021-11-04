
import pandas as pd
netflix_data= pd.read_csv("netflix_titles.csv")
#print(netflix_data)
#print(netflix_data.rating.value_counts())
#print(netflix_data.release_year.value_counts())
#print(netflix_data.country.value_counts())

values = netflix_data.country.value_counts()[:10].tolist()
labels = netflix_data.country.value_counts()[:10].index.tolist()
print(values)
print(labels)