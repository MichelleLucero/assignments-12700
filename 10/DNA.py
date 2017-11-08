"""
convert the DNA to its complement
practice to understand using empty strings
"""


strand = "ATGCATGC"
n_strand = ''
for i in strand:
    
    if i == 'A':
        n_strand = n_strand + 'T'
    if i == 'T':
        n_strand = n_strand + 'A'
    if i == 'C':
        n_strand = n_strand + 'G'
    if i == 'G':
        n_strand = n_strand + 'C'
        
print(n_strand)

    