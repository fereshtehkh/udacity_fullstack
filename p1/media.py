"""
The movie class contains the title, poster_url and trailer_url
"""
class Movie():
	def __init__(self, title, image_url, trailer_url):
		self.title = title
		self.poster_image_url = image_url
		self.trailer_youtube_url = trailer_url