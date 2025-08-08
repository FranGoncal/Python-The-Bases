def sub_cadeias(cadeia, n):

    for i in range(len(cadeia)+1 - n):
        print(cadeia[i:i+n])

sub_cadeias("ola mundo",3)