def sortList(lista: list):

    aux = None

    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux


    
