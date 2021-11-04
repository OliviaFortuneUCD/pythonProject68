import pandas as pd
netflix_data= pd.read_csv("netflix_titles.csv")
netflix_data.drop(['cast','description', 'director'], axis=1, inplace=True)
drop_duplicates= netflix_data.drop_duplicates(subset=['show_id'])
print(netflix_data.shape,drop_duplicates.shape)
