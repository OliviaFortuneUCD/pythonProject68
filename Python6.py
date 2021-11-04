
import pandas as pd
netflix_data= pd.read_csv("netflix_titles.csv")
#tv_show = netflix_data[netflix_data["type"] == "TV Show"]
#print(tv_show.head())
# Oldest Movie
# we want to descover yhe oldest movies
sort_data = netflix_data.sort_values("release_year", ascending = True)
print(sort_data[['title', "release_year"]][:15])
