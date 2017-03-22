import media;
import page;
import json;

with open('Data/movies.json') as movies:
        data = json.load(movies);

movies = []

for movie in data:
        newMovie = media.Movie(movie['title'], movie['description'], movie['cover'], movie['trailler']);
        movies.append(newMovie);

page.open_movies_page(movies);