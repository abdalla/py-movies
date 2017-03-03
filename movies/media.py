import webbrowser;

class Movie():
    def __init__(self, title, storyline, poster, ytb):
        self.title = title;
        self.storyline = storyline;
        self.poster_image_url = poster;
        self.trailer_youtube_url = ytb;

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url);

