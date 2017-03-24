import json

import media

import page


# Openning the JSON movies data
with open('Data/movies.json') as movies:
        data = json.load(movies)

movies = []
# Reading data and inserting in an array list to be generate the HTML
for movie in data:
	newMovie = media.Movie(movie['title'],
	                       movie['description'],
	                       movie['cover'],
	                       movie['trailler'])
	movies.append(newMovie)

page.open_movies_page(movies)
