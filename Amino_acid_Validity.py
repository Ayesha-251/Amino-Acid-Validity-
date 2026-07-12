#FOR DETERMINING THE INVALID AMINO ACID IN THE PROTEIN SEQUENCE AND UPDATING THE SEQUENCE BY REMOVING THE INVALID SEQUENCES 
protein=input("Enter a Protein Sequence: ").upper().strip()
corrected_sequence=""
Invalid_found = False 
for i in range(len(protein)):
    if protein[i] not in "ACDEFGHIKLMNPQRSTVWY":
        print(f"Invalid amino acid {protein[i]} at position {i}")
        Invalid_found=True 
        continue
    corrected_sequence=corrected_sequence+(protein[i])
if not Invalid_found:
    print("The Protein sequence is Valid")
else:
    print(f"Corrected sequence is {corrected_sequence}")
