import random
def guess():
    target = random.randint(0,13)

    i=0
    print("U get 7 tries!")

    while i<7:
        i+=1
        inp = input("Numero aleatorio entre 0 e 13?")
        if int(inp) == target:
            print("Winner! Num was "+ str(target) )
            return
    print("You lost!")

guess()