from media import Movie
import fresh_tomatoes

interstellar = Movie("Interstellar", "http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_UX182_CR0,0,182,268_AL_.jpg", "http://www.imdb.com/video/imdb/vi1586278169?ref_=tt_ov_vi")
dark_night = Movie("The Dark Knight Arises", "http://ia.media-imdb.com/images/M/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_UX182_CR0,0,182,268_AL_.jpg", "http://www.imdb.com/video/imdb/vi2376312089?ref_=tt_ov_vi")
frozen = Movie("Frozen", "http://ia.media-imdb.com/images/M/MV5BMTQ1MjQwMTE5OF5BMl5BanBnXkFtZTgwNjk3MTcyMDE@._V1_UX182_CR0,0,182,268_AL_.jpg", "http://www.imdb.com/video/imdb/vi2482677785?ref_=tt_ov_vi")

movies = [interstellar, dark_night, frozen]
fresh_tomatoes.open_movies_page(movies)