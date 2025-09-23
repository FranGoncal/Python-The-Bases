def treeVal(no: INode, profundidade: int) -> int:
    
    total = 0

    if no.isDangerous(): 
        try:
            total += no.getValue()
        except Exception as e:
            total -= profundidade
    else:
        total += no.getValue()

        for child in no.getChildren():
            total += treeVal(child, profundidade + 1)

    return total