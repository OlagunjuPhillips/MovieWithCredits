class Movie:
    def __init__(self, title, year, runtime, rating):
        self.title = title
        self.year = year
        self.runtime = runtime
        self.rating = rating

    def __str__(self):
        return '{self.title}, {self.runtime} minutes long, released in {self.year}, rated {self.rating}'.format(self = self)

    def getTitle(self):
        return self.title

    def getYear(self):
        return self.year

    def getRuntime(self):
        return self.runtime

    def getRating(self):
        return self.rating

    def setTitle(self, other):
        self.title = other

    def setYear(self, other):
        self.year = other

    def setRuntime(self, other):
        self.runtime = other

    def setRating(self, other):
        self.rating = other
