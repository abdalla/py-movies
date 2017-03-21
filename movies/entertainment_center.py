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

max_movie = media.Movie("MAX",
                        "After U.S. Marine Kyle Wincott is killed in Afghanistan, Max, his highly trained service dog, is too traumatized to remain in service. Back in the U.S., Kyle's family adopts the dog, but teenage brother Justin (Josh Wiggins) has problems of his own and doesn't want the animal. However, Max may be Justin's only chance to learn what really happened to his brother. With the help of a dog-savvy friend, Justin and Max begin to bond, and set out to unravel the mystery of Kyle's death.",
                        "http://t1.gstatic.com/images?q=tbn:ANd9GcRVbdwtE9pR0MR_5qtRqxkUqnHe1HJYe8pjuJsUQYFqDDJQFHox",
                        "https://youtu.be/6EPPMCwD5bw");

the_33 = media.Movie("The 33",
                        "In 2010, the eyes of the world turned to Chile, where 33 miners had been buried alive by the catastrophic explosion and collapse of a 100-year-old gold and copper mine.",
                        "http://cdn2-www.comingsoon.net/assets/uploads/gallery/the-33/the33_1sht_main_dom_2764x4096.jpg",
                        "https://youtu.be/hOoIBOYqHyw");

thertheen_hour = media.Movie("13 Hour",
                        "An attack takes place on the U.S. Special Mission Compound and a nearby CIA Annex in Benghazi on the eleventh anniversary of 9/11. Four Americans are killed in the attack, including U.S. Ambassador J. Christopher Stevens.",
                        "https://lh3.googleusercontent.com/E81guSjoP1LJsQnr693zUGyiwYjCEWJZsKjYUKvnLTHKAW68zBXF_3cpHAaGC1cfPkY_hw=w300",
                        "https://youtu.be/4CJBuUwd0Os");



movies = [toy_story, avatar, school_of_rock, max_movie, the_33, thertheen_hour];

page.open_movies_page(movies);

# print(media.Movie.__doc__);
# print(media.Movie.__name__);
# print(media.Movie.__module__);