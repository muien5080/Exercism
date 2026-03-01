def to_rna(dna_strand):
    translation_table = str.maketrans({
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U",
    })
    return dna_strand.translate(translation_table)