#Substituindo caractere repetido
gameName = "The Last Of Us"
char = gameName[0].lower()
newWord = gameName.replace(char,'$')
newWord = char + newWord[1:]
print(newWord)

#Troca de caracteres
word1 = 'abc'
word2 = 'def'
newWord1 = word2[:2] + word1[2:]
newWord2 = word1[:2] + word2[2:]

print(f"{newWord1} {newWord2}")