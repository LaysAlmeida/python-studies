import json

#1 - Essa variável JSON ficou armazenada como string - Strings para Dicionários
person = '{"name": "Lays", "languages":["Python", "Javascript"]}'
person_dict = json.loads(person)
print(person_dict)
print(person_dict['languages'])
print(person_dict['languages'][0])

# 2 - Convertendo dicionário para JSON
person_json = json.dumps(person_dict)
print(person_json)
print(type(person_json))

# 3 - Formatando JSON
print(json.dumps(person_dict, indent=4, sort_keys= True))

#4 - Salvando JSON em txt
with open("person.txt", "w") as json_file:
    json.dump(person_dict, json_file)
    
# 5 - Ler JSON externo    #Se não passar o parametro, ele tem como padrao o r
with open("example.json", "r") as f:
    data = json.load(f) #Vai transformar em um dicionário
    print(data)
    print(type(data))
    print(data['courses'][1]['language']) #JavaScript
    
#6 - Selecionando curso pelo nomeno arquivo json numa estrutura aninhada
    for course in data['courses']:
        if course['language'] == "Javascript":
            print(course['level'])
            assert course['level'] == "Beginner"