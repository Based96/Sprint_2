class Movies:
    def __init__(self,):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f'Комедии: {self.movies}'

class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f'Драмы: {self.movies}'

comedy = Comedy()
movie_comedy = comedy.add_movie ('Большой куш')
print(movie_comedy)

drama = Drama()
movie_drama = drama.add_movie('Оружейный барон')
print(movie_drama)