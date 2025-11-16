class Movie:
    def __init__(self, name, yearLaunch, includedPlan, note, movieDuration):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
        self.movieDuration = movieDuration
    def __str__(self):
        return f"Filme: {self.name}  \nAno de Lançamento: {self.yearLaunch} \nIncluso no Plano: {self.includedPlan} \nAvaliação: {self.note} \nDuração: {self.movieDuration}"     
        
movieInfo = Movie("Jogos vorazes", 2012, True, 7.2, 144)
# print(movieInfo.name)
print(movieInfo)