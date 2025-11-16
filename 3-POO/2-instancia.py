class Movie:
    movieName = ""
    yearLaunch = 0
    includedPlan = False
    note = 0
    movieDuration = 0
    
# Primeiro Filme#
movie = Movie() #Instância da classe
movie.movieName = "The Hunger Games"
movie.yearLaunch = 2012
movie.includedPlan = True
movie.note = 7.2
movie.movieDuration = 142
print("Dados do filme")
print(f"Nome fo filme: {movie.movieName} \nAno de Lançamento: {movie.yearLaunch} \nIncluso no Prime Video: {movie.includedPlan} \nAvaliações: {movie.note} estrelas \nTempo de duração do filme: {movie.movieDuration}min")  #Retorna a classe Movie e e um objeto