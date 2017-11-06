import webbrowser


class Movie():
    """ Movie properties: title, storyline, poster image and trailer url """

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """ Initializing title, storyline, poster_image_url,
        and trailer_youtube_url instance variables. """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Open URL via webbrowser """
        webbrowser.open(self.trailer_youtube_url)
