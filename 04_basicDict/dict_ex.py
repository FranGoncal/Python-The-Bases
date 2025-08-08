cientistas = {'Newton': 1642, 'Darwin': 1809, 'Turing': 1912}

#a) Acrescente um elemento novo ao dicionário
cientistas ["Pou"] = 11
print(cientistas)

#b) Altere a data de nascimento de um autor
cientistas ["Pou"] = 112
print(cientistas)

#c) Remova um elemento do dicionário
cientistas.pop("Pou")
print(cientistas)

#d) Calcule o número de elementos de um dicionário
len(cientistas.values())

#e) Determine se existe uma dada entrada no dicionário
if "Nelson" in cientistas:
    print("ai ta ele")

#f) Faça uma cópia do dicionário
cie = cientistas.copy()
#g) Limpe a versão original do dicionário
cientistas.clear()

print(cientistas)

print(cie)
