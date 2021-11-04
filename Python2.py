import pandas as pd
netflix_data= pd.read_csv("netflix_titles.csv")
netflix_data.drop(['cast','description', 'director'], axis=1, inplace=True)
print(netflix_data)
missing_values_count = netflix_data.isnull().sum()
print(missing_values_count[0:5])