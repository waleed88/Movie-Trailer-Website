import fresh_tomatoes
import media

# toy_story movie: movie_title, storyline, poster_image and movie trailer
toy_story = media.movie(
    "Toy Story",
    "Toy Story was the first feature-length computer-animated film "
    "and the first feature film produced by Pixar",
    "https://vignette.wikia.nocookie.net/disney/i"
    "mages/1/13/Toy_Story.jpg/revision/latest?cb=20151003163558",
    "https://www.youtube.com/watch?v=4KPTXpQehio"
                        )

# avatar movie: movie_title, storyline, poster_image and movie trailer
avatar = media.movie(
    "Avatar",
    "The film is set in the mid-22nd century,"
    "when humans are colonizing",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
                     )

# m_impossible movie: movie_title,storyline,poster_image and movie trailer

mission_impossible = media.movie(
    "MI6",
    "When an IMF mission ends badly,"
    "the world is faced with dire consequences",
    "https://upload.wikimedia.org/wikipedia/en/f/ff/MI_%E2%80%93_Fallout.jpg",
    "https://www.youtube.com/watch?v=wb49-oV0F78&t=16s"
                                 )

# suits movie: movie_title, storyline, poster_image and movie trailer
suits = media.movie(
    "suits",
    "Mike enters the Federal prison in"
    "Danbury to face his two-year jail sentence for fraud",
    "https://upload.wikimedia.org/wikipedia/en/thumb/7/7e/"
    "Suits_Season_6_DVD_Cover.jpg/220px-Suits_Season_6_DVD_Cover.jpg",
    "https://www.youtube.com/watch?v=Ab2YIbP5xw8"
                   )


# set the movies that will be passed to the media file
movies = [toy_story, avatar, mission_impossible, suits]

# open the html file in a webbrowser via the fresh_tomatoes file,
fresh_tomatoes.open_movies_page(movies)

print(media.movie.__module__)
