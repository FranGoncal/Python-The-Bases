'''
Write a function to check if two strings are anagrams.
'''


def anagram_check(s1, s2):
    d1={}
    d2={}

    
    for letra in s1:
        if letra not in d1:
            d1[letra] = 1
        else:
            d1[letra] += 1

    for letra in s2:
        if letra not in d2:
            d2[letra] = 1
        else:
            d2[letra] += 1
            
    return d1 == d2

print(anagram_check("listen","silent"))