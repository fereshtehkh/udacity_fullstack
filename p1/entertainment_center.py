from media import Movie
import fresh_tomatoes

# movie instantiation
interstellar = Movie("Interstellar",
                     "http://ia.media-imdb.com/images/M" +
                     "/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                     "https://www.youtube.com/watch?v=2LqzF5WauAw")
dark_night = Movie("The Dark Knight Arises",
                   "http://ia.media-imdb.com/images/M" + 
                   "/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                   "https://www.youtube.com/watch?v=g8evyE9TuYk")
frozen = Movie("Frozen",
               "http://ia.media-imdb.com/images/M" +
               "/MV5BMTQ1MjQwMTE5OF5BMl5BanBnXkFtZTgwNjk3MTcyMDE@._V1_UX182_CR0,0,182,268_AL_.jpg",
               "https://www.youtube.com/watch?v=TbQm5doF_Uc")

# movie collection
movies = [interstellar, dark_night, frozen]

# generate markup in fresh_tomatoes.html
fresh_tomatoes.open_movies_page(movies)
