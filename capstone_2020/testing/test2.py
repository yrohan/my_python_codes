import pandas as pd

my_data=pd.read_csv("C:/Users/Linux/PycharmProjects/capstone_2020/datasets/imdb-data-of-watchedrated-movies/ratings.csv",delimiter=',')



print(my_data.shape)
print(my_data["Title"][0])
print(my_data["Genres"][0])
print(my_data["Directors"][0])
print(my_data["Your Rating"][0])
print(my_data["IMDb Rating"][0])
