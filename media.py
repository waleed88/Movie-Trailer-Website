import webbrowser
class movie():
    """this class provide a way to store movie related info"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
       """the def_init method initialized pieses of varivales like tilte,story line"""
       """,poster_image,trailer_youtube inside the class"""
       self.title = movie_title
       self.storyline = movie_storyline
       self.poster_image_url = poster_image
       self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """the show_trailer mothod to playing movie trailer"""
        webbrowser.open(self.tariler_youtube_url)


        
    
