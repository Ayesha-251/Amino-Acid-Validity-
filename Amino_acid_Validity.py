#FOR DETERMINING ONLY THE INVALID AMINO ACID IN THE PROTEIN SEQUENCE     
protein=input("Enter a Protein Sequence: ").upper().strip()
Invalid_found = False 
for i in range(len(protein)):
    if protein[i] not in "ACDEFGHIKLMNPQRSTVWY":
        print(f"Invalid amino acid {protein[i]} at position {i}")
        Invalid_found=True 
if not Invalid_found:
    print("The Protein sequence is Valid")
