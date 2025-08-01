
class MediaCollection:
    def __init__(self, movie_list, game_list):
        self.movie_list = movie_list
        self.game_list = game_list
        self.fav_game = ""
        self.fav_movie = ""

    def add_movie(self, movie):
        self.movie_list.append(movie)

    def add_game(self, game):
        if game in self.game_list:
            print("Game is already in collection")
        else:
            self.game_list.append(game)

    def remove_game(self, game):
        if game in self.game_list:
            self.game_list.remove(game)
        else:
            print("Game not found")

    def remove_movie(self, movie):
        if movie in self.movie_list:
            self.movie_list.remove(movie)
        else:
            print("Movie not found")

    def display_games(self):
        print("Games in collection:")
        for game in self.game_list:
            print(f"- {game}")

    def display_movies(self):
        print("Movies in collection:")
        for movie in self.movie_list:
            print(f"- {movie}")

    def display_fav_movie(self):
        print(f"Favorite Movie: {self.fav_movie}")

    def display_fav_game(self):
        print(f"Favorite Game: {self.fav_game}")

    def display_collection(self):
        self.display_movies()
        self.display_fav_movie()
        self.display_games()
        self.display_fav_game()

    def set_fav_movie(self, movie):
        if movie not in self.movie_list:
            self.add_movie(movie)
        self.fav_movie = movie

    def set_fav_game(self, game):
        if game not in self.game_list:
            self.add_game(game)
        self.fav_game = game

