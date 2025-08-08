def mod_str(pos,strg,ch):
    if pos > len(strg):
        return
    
    strg = strg[:pos-1]+ch+strg[pos:]
    
    return strg

print(mod_str(3,"0123456789","X"))

print(mod_str(1,"0123456789","X"))

print(mod_str(9,"0123456789","X"))

print(mod_str(11,"0123456789","X"))