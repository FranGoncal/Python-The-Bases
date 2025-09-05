'''
Find the first non-repeating character in a string.
'''


dicionario = {}
palavra = "palavrap"
print(palavra)

for letra in palavra:
    if letra not in dicionario:
        dicionario[letra] = 1
    else:
        dicionario[letra] += 1

for letra in palavra:
    if dicionario[letra] == 1:
        print(letra)
        break
