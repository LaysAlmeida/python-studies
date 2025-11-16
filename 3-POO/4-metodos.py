class Movie:
    def __init__(self, name, yearLaunch, includedPlan, note, movieDuration):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
        self.movieDuration = movieDuration
    
    def __str__(self):
        return f"Filme: {self.name}"     
    
    def technical_sheet(self):
        print("##Dados do filme##")
        print(f"Nome do filme: {self.name}")
        print(f"Ano de Lançamento: {self.yearLaunch}")
        print(f"Está incluso no plano? {self.includedPlan}")
        print(f"Avaliação do filme: {self.note}")
        print(f"Duração do filme: {self.movieDuration}")
        
hungerGames = Movie("Jogos vorazes", 2012, True, 7.2, 144)

hungerGames.technical_sheet()