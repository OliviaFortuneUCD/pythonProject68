# Simple & Easy way to overview dataset

import pandas as pd
netflix_data= pd.read_csv("netflix_titles.csv")
netflix_data.drop(['cast','description', 'director'], axis=1, inplace=True)

country_share = netflix_data.mean().sort_values(ascending=False).round(4) * 100
print(country_share)
