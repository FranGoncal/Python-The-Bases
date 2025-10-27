def findMax(lista: list):
    
    if len(lista) == 0:
        return None
    
    max = lista.pop()

    for numero in lista:
        if numero > max:
            max = numero
    
    return max

print(findMax([]))