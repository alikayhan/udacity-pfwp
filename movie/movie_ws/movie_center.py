__author__ = 'alikayhan'


import movie
import fresh_tomatoes

toy_story = movie.Movie("Toy Story",
                        "Story of a boy and his toy.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.title)

avatar = movie.Movie("Avatar",
                     "A marine on an alien planet.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.storyline)
#avatar.show_trailer()

battleship_potemkin = movie.Movie("Battleship Potemkin",
                                  "Mutiny by the crew of the Russian battleship Potemkin rebelled against their officers of the Tsarist regime.",
                                  "https://upload.wikimedia.org/wikipedia/commons/8/85/Vintage_Potemkin.jpg",
                                  "https://www.youtube.com/watch?v=x4opFQ7Drco")

#battleship_potemkin.show_trailer()

movies = [toy_story, avatar, battleship_potemkin]
fresh_tomatoes.open_movies_page(movies)

# print(movie.Movie.__doc__)
# print(movie.Movie.VALID_RATINGS)
# print(movie.Movie.__name__)
# print(movie.Movie.__module__)