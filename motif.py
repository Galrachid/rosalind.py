#Giselle Alrachid 
#7 May 2020

#Input of given values
N = 90000
x = 0.6
s = 'ATAGCCGA'
AT = 0
GC = 0
#Based off of given definition. 
for nt in s:
    if nt == 'A' or nt == 'T':
        AT += 1
    elif nt == 'G' or nt == 'C':
        GC += 1
#calculates based of given equation
s_prob = (((1 - x) / 2)**AT) * (((x) / 2)**GC)
prob = 1 - (1 - s_prob)**N
print('%0.3f' % prob)
