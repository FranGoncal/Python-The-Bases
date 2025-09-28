def divisao(a, b):
    
    try:
        res = a / b
    except Exception as e:
        return "Divisão por zero não é permitida."
    return res

print(divisao(2,3))

print(divisao(2,5))

print(divisao(2,0))

print(divisao(21,2))

print(divisao(2,0))
