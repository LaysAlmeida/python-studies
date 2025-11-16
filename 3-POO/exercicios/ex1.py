class Movie:
    def __init__(self, name, yearLaunch, includedPlan, movieDuration):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.totalEvaluation = 0
        self.totalEvaluators = 0
        self.movieDuration = movieDuration
    
    def __str__(self):
        return f"Filme: {self.name}"     
    
    def technical_sheet(self):
        print("##Dados do filme##")
        print(f"Nome do filme: {self.name}")
        print(f"Ano de Lançamento: {self.yearLaunch}")
        print(f"Está incluso no plano? {self.includedPlan}")
        print(f"Sua última avaliação do filme: {self.personalEvaluation}")
        print(f"Média de avaliação do filme: {self.average}")
        print(f"Duração do filme: {self.movieDuration}")
        print(f"Quantidade de avaliações do filme: {self.totalEvaluators}")
        
    def ratingMovie(self, note):
        self.totalEvaluation += note
        self.totalEvaluators += 1
        self.personalEvaluation = note  
          
    def evaluationRate (self):
        self.average = f"{(self.totalEvaluation)/self.totalEvaluators:.1f}" 
        
hungerGames = Movie("Jogos vorazes", 2012, True, 144)

hungerGames.ratingMovie(9.0)
hungerGames.ratingMovie(10.0)
hungerGames.ratingMovie(6.0)

hungerGames.evaluationRate()
hungerGames.technical_sheet()