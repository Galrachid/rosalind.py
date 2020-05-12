#Giselle Alrachid 
#12 May 2020

import math

#Using mathfactorial i plugged in the values I was given (n,k,n-k...)
def variable(n, k, p):
    return (math.factorial(n) / math.factorial(k) / math.factorial(n-k)) * (p**k * (1-p)**(n-k))
#Sample number
n = 5

#Using Probability in python
prob = []
for k in range(2*n, -1, -1):
    prob = prob + [variable(n*2, k, 0.5)]
#Given equation
prob = [math.log10(sum(prob[:i])) for i in range(2*n, 0, -1)]

#Print final values 
print(' '.join([str(i) for i in prob]))
