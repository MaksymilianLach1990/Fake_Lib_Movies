import random

class Film:
    def __init__(self, name, year, sort):
        self.name = name
        self.year = year
        self.sort = sort

        self.number_of_plays = 0

    def __str__(self):
        return f'{self.name} ({self.year})'

    def __repr__(self):
        return f'Film(name={self.name}, year={self.year}, sort={self.sort}'

    def play(self, step=1):
        self.number_of_plays += step


class Serial(Film):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f'{self.name} S{self.season}E{self.episode}'

    def __repr__(self):
        return f'Serial(name={self.name}, season={self.season}, episode={self.episode}, year={self.year}, sort={self.sort}'


def get_movies():
    list_movies = []
    return sorted(list_movies)

def get_series():
    list_series = []
    return sorted(list_series)

def search(name):
    pass

def generate_views():
    movie = random(films_end_series)

def top_titles(content_type):
    pass

films_end_series = []