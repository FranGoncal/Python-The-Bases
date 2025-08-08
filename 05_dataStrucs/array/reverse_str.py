def reverse_basic(string):

    if string == None or len(string) < 2 or not isinstance(string, str):
        return "Input Problem"
    
    return string[::-1]

def reverse_w_array(string):
    if string == None or len(string) < 2 or not isinstance(string, str):
        return "Input Problem"
    
    arra = []

    for l in range(len(string)-1,-1,-1):
        arra.append(string[l])
    
    string = ""

    for l in arra:
        string += l

    return string



print(reverse_basic("Hi my name is Francisco"))
print(reverse_basic(""))
print(reverse_basic("H"))

print("\n")

print(reverse_w_array("Hi my name is Francisco"))
print(reverse_w_array(""))
print(reverse_w_array("H"))