
def remover_repetidos_set(lista):
    set_aux = set()

    for elemento in lista:
        set_aux.add(elemento)
    
    lista = []
    
    for elemento in set_aux:
        lista.append(elemento)
    
    return lista


def remover_repetidos_dict(lista):
    dicionario = {}

    for elemento in lista:
        dicionario[elemento] = True
    
    lista = []

    for elemento in dicionario.keys():
        lista.append(elemento)
    
    return lista



print(remover_repetidos_dict([1,2,3,4,66,7,9,8,4,6,2,29,3,4,5,6,7,8,9,1,2,3,4,5,6,7000]))