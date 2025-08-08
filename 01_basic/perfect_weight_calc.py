def weight_calc():
    height = input("What is ur height?")
    g = input("Are u a male (m) or female (f)?")


    if g == "m":
        weight = 72.7 * float(height) - 58
    elif g == "f":
        weight = 62.1 * float(height) - 44.7
    else:
        print("No case matches " + g)
        exit()
        

    print("Your perfect weight is " + str(weight) + "\n")

weight_calc()