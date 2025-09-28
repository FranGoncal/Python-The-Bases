def conta_elementos(lista: list)-> int:
    n_elementos = 0
    for elemento in lista:
        if isinstance(elemento, int):
            n_elementos += 1
        elif isinstance(elemento, list):
            n_elementos += conta_elementos(elemento)
    
    return n_elementos


lista = [[1, [2, [3, 4], 5], 6],[[1,2,3,4,5,5],[[3,3],[1]]]]

print(conta_elementos(lista))