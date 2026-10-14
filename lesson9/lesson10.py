from Bio import SeqIO

for record in SeqIO.parse("COX1.FASTA", "fasta"):
    print(record.id)
    print(record.description)
    print(len(record))
    print("z"*30)