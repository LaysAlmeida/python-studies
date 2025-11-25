name = input("Digite o seu nome: ")

# Alternativa 1 -> Vai adicionar o nome no arquivo names.txt, mas a cada execução sobrescreve o nome anterior com o novo
# file = open("names.txt", "w")
# file.write(name)
# file.close()

# Alternativa 1.1 -> Vai adicionar o nome no arquivo txt sem sobrescrever o anterior e depois vai fechar
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

#Alternativa 2 -> Utilizando o contexto com o with, vai fazer todos os passos como os acima, mas de forma refatorada
with open("files/names.txt", "a") as file:
    file.write(f"{name}\n")