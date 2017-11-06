import media
import fresh_potatoes


#  Thor: Ragnarok movie: movie title, storyline, poster image and trailer url
thor_ragnarok = media.Movie("Thor: Ragnarok",  # movie title
                            "Imprisoned, the mighty Thor finds "  # storyline
                            "himself in a lethal gladiatorial contest against "
                            "the Hulk, his former ally. Thor must fight for "
                            "survival and race against time to prevent the "
                            "all-powerful Hela from destroying his home and "
                            "the Asgardian civilization.",
                            "https://images-na.ssl-images-"  # poster image
                            "amazon.com/images/M/MV5BMjMyNDkzMzI1OF5BMl5Ban"
                            "BnXkFtZTgwODcxODg5MjI@._V1_SY1000_CR0,0,674,"
                            "1000_AL_.jpg",
                            "https://www.youtube.com/"  # trailer url
                            "watch?v=ue80QwXMRHg")


#  Jigsaw movie: movie title, storyline, poster image and trailer url
jigsaw = media.Movie("Jigsaw",  # movie title
                     "Bodies are turning up around the city, "  # story line
                     "each having met a uniquely gruesome demise. "
                     "As the investigation proceeds, evidence "
                     "points to one suspect: John Kramer, the man "
                     "known as Jigsaw, who has been dead for ten years.",
                     "https://images-na.ssl-images-"  # poster image
                     "amazon.com/images/M/MV5BNmRiZDM4ZmMtOTVjMi00YTNlLTkyNjMt"
                     "MjI2OTAxNjgwMWM1XkEyXkFqcGdeQXVyMjMxOTE0ODA@."
                     "_V1_SY1000_CR0,0,648,1000_AL_.jpg",
                     "https://www.youtube.com/"  # trailer url
                     "watch?v=vPP6aIw1vgY")


#  Blade Runner 2049: movie title, storyline, poster image and trailer url
blade_runner = media.Movie("Blade Runner 2049",  # movie title
                           "A young blade runner's discovery "  # storyline
                           "of a long-buried secret leads him"
                           "to track down former blade runner Rick Deckard,"
                           "who's been missing for thirty years.",
                           "https://images-na.ssl-images-"  # poster image
                           "amazon.com/images/M/MV5BNzA1Njg4NzYxOV5BMl5Ban"
                           "BnXkFtZTgwODk5NjU3MzI@._V1_SY1000_CR0,0,674,"
                           "1000_AL_.jpg",
                           "https://www.youtube.com/"  # trailer url
                           "watch?v=gCcx85zbxz4")


#  Only the Brave movie:movie title, storyline, poster image and trailer url
only_the_brave = media.Movie("Only the Brave",  # movie title
                             "Based on the true story of the "  # storyline
                             "Granite Mountain Hotshots, a group of elite "
                             "firefighters risk everything to protect a town "
                             "from a historic wildfire.",
                             "https://images-na.ssl-images-"  # poster image
                             "amazon.com/images/M/MV5BMTY5ODc5OTc2M15BMl5Ban"
                             "BnXkFtZTgwNjM0NjIzMzI@._V1_.jpg",
                             "https://www.youtube.com/"  # trailer url
                             "watch?v=EE_GY6zccqc")

#  The Foreigner movie: movie title, storyline, poster image and trailer url
the_foreigner = media.Movie("The Foreigner",  # movie title
                            "A humble businessman with a buried "  # storyline
                            "past seeks justice when his daughter is killed "
                            "in an act of terrorism. A cat-and-mouse conflict "
                            "ensues with a government official, whose past "
                            "may hold clues to the killers' identities.",
                            "https://images-na.ssl-images-"  # poster image
                            "amazon.com/images/M/MV5BM2RlMjcyMGQtZTU3OC00NG"
                            "RlLWExMGEtYjU3ZjUyMDc0NWZmXkEyXkFqcGdeQXVyNTI4M"
                            "zE4MDU@._V1_SY1000_SX675_AL_.jpg",
                            "https://www.youtube.com/"  # trailer url
                            "watch?v=33iuQu3UtjI")


#  It movie: movie title, storyline, poster image and trailer url
it = media.Movie("It",  # movie title
                 "A group of bullied kids band together "  # storyline
                 "when a shapeshifting demon, taking the appearance of "
                 "a clown, begins hunting children.",
                 "https://images-na.ssl-images-"  # poster image
                 "amazon.com/images/M/MV5BOTE0NWEyNDYtYWI5MC00MWY"
                 "0LTg1NDctZjAwMjkyMWJiNzk1XkEyXkFqcGdeQXVyNjk5NDA3OTk@."
                 "_V1_SY1000_CR0,0,674,1000_AL_.jpg",
                 "https://www.youtube.com/"  # trailer url
                 "watch?v=hAUTdjf9rko")


#  Set of movie instances that will be passed to the media file
movies = [
    thor_ragnarok,
    jigsaw,
    blade_runner,
    only_the_brave,
    the_foreigner,
    it
    ]


#  Create HTML file then Open it in a webbrowser via fresh_potatoes.py file
fresh_potatoes.open_movies_page(movies)
