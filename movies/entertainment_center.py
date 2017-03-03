import media;
import page;

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://youtu.be/KYz2wyBy3kc");

avatar = media.Movie("Avatar",
                        "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=d1_JBMrrYw8");

school_of_rock = media.Movie("School of Rock",
                        "After being kicked out of a rock band, Dewey Finn becomes a substitute teacher of a strict elementary private school, only to try and turn it into a rock band.",
                        "http://www.gstatic.com/tv/thumb/movieposters/33094/p33094_p_v8_aa.jpg",
                        "https://youtu.be/XCwy6lW5Ixc");


movies = [toy_story, avatar, school_of_rock];

#page.open_movies_page(movies);

print(media.Movie.__doc__);
print(media.Movie.__name__);
print(media.Movie.__module__);