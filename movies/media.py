import webbrowser


# Class used as model for movies.
class Movie():
	# Movie Constructor
    def __init__(self, title, storyline, poster, ytb):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = ytb

   # Function used to open popup to present the trailer and movie synopsis
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
