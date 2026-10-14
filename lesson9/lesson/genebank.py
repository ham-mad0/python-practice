from Bio import SeqIO

record = SeqIO.read("mesh.gb", "genbank")
print(record.id)
print(record.description)
print(record.annotations)

print(len(record.features))

for feature in record.features:
    print(feature.type)
    print(feature.location)