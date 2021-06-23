import random
from faker import Faker
fake= Faker()

""" Pamiętaj:
    
    -sezon i epizot dodaj '0' """


class Film:
    def __init__(self, name, year, sort):
        self.name = name.title()
        self.year = year
        self.sort = sort.title()

        self.number_of_plays = 0

    def __str__(self):
        return f'{self.name} ({self.year})'

    def __repr__(self):
        return 'Film(name={}, year={}, sort={}'.format(self.name, self.year, self.sort)

    def play(self, step=1):
        self.number_of_plays += step


class Serial(Film):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode

    def __str__(self):
        if self.season < 10:
            self.season = '0{}'.format(self.season)
        if self.episode < 10:
            self.episode = '0{}'.format(self.episode)
        return f'{self.name} S{self.season}E{self.episode}'

    def __repr__(self):
        return f'Serial(name={self.name}, season={self.season}, episode={self.episode}, year={self.year}, sort={self.sort}'
    
    

films_end_series = []


def get_movies(lista):
    list_movies = []
    for movie in lista:
        if isinstance(movie, Film) == True:
            list_movies.append(movie)
    return sorted(list_movies, key=lambda film: film.name)

def get_series(lista):
    list_series = []
    for series in lista:
        if isinstance(series, Serial) == True:
            list_series.append(series)
    return sorted(list_series, key=lambda serie: serie.name)

def search(name, lista):
    if name is lista:
        print(f'{name} jest na liście.')
    else:
        print(f'{name} nie ma na liście.')

def generate_views(lista):
    number = random.randint(0, len(lista)-1)
    lista[number].play(random.randint(1, 100))

def multi_generate(lista):
    for number in range(10):
        generate_views(lista)

def top_titles(number, library, content_type='all'):

    ranking = sorted(library, key=lambda ranking: ranking.number_of_plays)
    ranking.reverse()
    for title in range(number):
        print(ranking[title])

def add_season(serial_name, serial_year, serial_sort, number_season, count_episode, library):
    for number in range(1, count_episode+1):
        library.append(Serial(name=serial_name, year=serial_year, sort=serial_sort, season=number_season, episode=number))


if __name__ == '__main__':

    movie_sort = ['bajka', 'akcja', 'kryminał', 'biografia']


    add_season('Simson', '1990', 'bajka', 2, 12, films_end_series)



    for movie in range(100):
        films_end_series.append(Film(name=fake.word(), year=fake.year(), sort=movie_sort[random.randint(0, len(movie_sort)-1)]))
        films_end_series.append(Serial(name=fake.word(), season=random.randint(1, 10), episode=random.randint(1, 27), year=fake.year(), sort=movie_sort[random.randint(0, len(movie_sort)-1)]))

    print(films_end_series[0].number_of_plays)
    generate_views(films_end_series)
    multi_generate(films_end_series)
    top_titles(3, films_end_series)