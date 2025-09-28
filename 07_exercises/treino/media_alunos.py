def media_alunos(dicionario: dict) -> dict:
    
    media_notas = {}

    for aluno in dicionario.keys():
        
        soma = 0
        notas = 0
        media = 0

        for nota in dicionario[aluno].keys():
            notas += 1
            
            soma += dicionario[aluno][nota]
        
        media = soma / notas

        media_notas[aluno] = media
    
    return media_notas

def apresenta_notas(dicionario: dict):
    for aluno in dicionario.keys():
        print("Aluno: " + aluno + "\nMédia: " + str(dicionario[aluno]) + "\n")

dicionario={
            "Jesus": {"Teste1" : 12.1, "Teste2" : 16.2},
            "Maria": {"Teste1" : 9, "Teste2" : 10},
            "Mafalda": {"Teste1" : 9.5, "Teste2" : 9.5},
            "Zacarias": {"Teste1" : 2.2, "Teste2" : 14},
            "Pumba": {"Teste1" : 11.9, "Teste2" : 11.1},
            "Paulo": {"Teste1" : 5.6, "Teste2" : 16.7},
            "Marco": {"Teste1" : 14.6, "Teste2" : 11.5},
            "Ribeiro": {"Teste1" : 15.5, "Teste2" : 18}
            }


dicionario = media_alunos(dicionario)
apresenta_notas(dicionario)