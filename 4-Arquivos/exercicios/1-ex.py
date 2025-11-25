def read_albumns_by_requested_index(linesNumber, fileName):
   names = []
   
   with open(fileName, encoding="utf-8") as file:
    for line in file:
        names.append(line.rstrip())       
   
   for name in range(linesNumber):
    print(names[name])
    
#Outra forma de fazer:
# def read_albumns_by_requested_index(linesNumber, fileName):
#     with open(fileName, encoding="utf-8") as file:
#         for i in range(linesNumber):
#             line = file.readline() #Lê uma linha por vez e armazena o valor para printar
#             if not line:   # acabou o arquivo
#                 break
#             print(line.rstrip())    
    
read_albumns_by_requested_index(5, 'albuns_ts.txt')                  