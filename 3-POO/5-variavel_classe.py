class Movie:
    platform = 'Prime Video' #Variável de classe
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
        print(f"Plataforma: {Movie.platform}")
        
hungerGames = Movie("Jogos vorazes", 2012, True, 7.2, 144)
hungerGames.technical_sheet()

tsitp = Movie("The Summer I Turned Pretty", 2026, True, 10, 144)
Movie.platform = 'Cinema' #Modificando o valor da variável de classe
tsitp.technical_sheet()