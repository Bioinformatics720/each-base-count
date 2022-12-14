dna = input("enter DNA sequence:")
dna_seq=["A", "T", "C", "G"]
for base in dna_seq:
    basecount=dna.count(base)
    print(base,basecount)
