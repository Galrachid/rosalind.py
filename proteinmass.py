#Giselle Alrachid 
# 11 May 2020

#Example given on the website 
sequence = 'SKADYEK'
#Values given on the website
Values = {'A': 71.04, 'C': 103.01, 'D': 115.03, 'E': 129.04, 'F': 147.07,
       'G': 57.02, 'H': 137.06, 'I': 113.08, 'K': 128.09, 'L': 113.08,
       'M': 131.04, 'N': 114.04, 'P': 97.05, 'Q': 128.06, 'R': 156.10,
       'S': 87.03, 'T': 101.05, 'V': 99.07, 'W': 186.08, 'Y': 163.06 }
#Adds up values of proteins
Values = sum(Values[p] for p in sequence)
print ("The molecular weight of the protein is", Values)
