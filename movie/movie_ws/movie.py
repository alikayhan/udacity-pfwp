__author__ = 'alikayhan'


import webbrowser


class Movie:
    """This class provides a way to store movie related information."""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title,
                 storyline,
                 poster_image,
                 trailer):

        self.title = title
        self.storyline = storyline
        self.poster_image = poster_image
        self.trailer = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
