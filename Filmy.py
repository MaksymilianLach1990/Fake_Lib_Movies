

class Film:
    def __init__(self, name, year, sort):
        self.name = name
        self.year = year
        self.sort = sort

        self.number_of_plays = 0

    def play(self, step=1):
        self.number_of_plays += step

class Serial(Film):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode
