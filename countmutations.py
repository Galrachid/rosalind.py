#Giselle Alrachid 
#May 5 2020

def countmutations(s, t):
    l = min(len(s), len(t))
    result = abs(len(s) - len(t))
    for i in range(0, l):
        if s[i] != t[i]:
            result += 1
    return result

s = 'GAGCCTACTAACGGGAT'
t = 'CATCGTAATGACGGCCT'

print (countmutations(s, t))
