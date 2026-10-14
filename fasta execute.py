from Bio import SeqIO

record = SeqIO.read("NM_000059.fasta", "fasta")
print(record.id)
print(record.description)
print(record.annotations)

print(len(record.features))

for feature in record.features:
    print(feature.type)
