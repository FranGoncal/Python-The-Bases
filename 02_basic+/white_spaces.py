def white(cadeia):
    vogais = ["a","e","i","o","u","A","E","I","O","U"]

    for i in range(1,len(cadeia)):
        if cadeia[i-1] in vogais:
            cadeia = substituir(i, cadeia, " ")
    return cadeia

def substituir(pos, cadeia, new):
    return cadeia[:pos-1] + new + cadeia[pos:]


print(white("aAjkikekEloiUp"))