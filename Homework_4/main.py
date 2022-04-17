# Homework question 4A
def pattern_trans(rna, gen_code):
    triple_k_mer = []
    peptide = []
    for i in range(0, len(rna)):
        triple_k_mer.append(rna[i:i + 3])
    for i in range(0, len(triple_k_mer)):
        if triple_k_mer[i] == ("UUU" or "UUC"):
            peptide.append("Phe")
        elif triple_k_mer[i] == ("UUA" or "UUG" or "CUU" or "CUC" or "CUA" or "CUG"):
            peptide.append("Leu")
        elif triple_k_mer[i] == ("AUU" or "AUC" or "AUA"):
            peptide.append("Ile")
        elif triple_k_mer[i] == ("GUU" or "GUC" or "GUA" or "GUG"):
            peptide.append("Val")
        elif triple_k_mer[i] == ("UCU" or "UCC" or "UCA" or "UCG"):
            peptide.append("Ser")
        elif triple_k_mer[i] == ("CCU" or "CCC" or "CCA" or "CCG"):
            peptide.append("Pro")
        elif triple_k_mer[i] == ("ACU" or "ACC" or "ACA" or "ACG"):
            peptide.append("Thr")
        elif triple_k_mer[i] == ("GCU" or "GCC" or "GCA" or "GCG"):
            peptide.append("Ala")
        elif triple_k_mer[i] == ("UAC" or "UAU"):
            peptide.append("Tyr")
        elif triple_k_mer[i] == ("CAU" or "CAC"):
            peptide.append("His")
        elif triple_k_mer[i] == ("CAA" or "CAG"):
            peptide.append("Gln")
        elif triple_k_mer[i] == ("AAU" or "AAC"):
            peptide.append("Asn")
        elif triple_k_mer[i] == ("AAA" or "AAG"):
            peptide.append("Lys")
        elif triple_k_mer[i] == ("GAU" or "GAC"):
            peptide.append("Asp")
        elif triple_k_mer[i] == ("GAA" or "GAG"):
            peptide.append("Glu")
        elif triple_k_mer[i] == ("UGU" or "UGC"):
            peptide.append("Cys")
        elif triple_k_mer[i] == "UGG":
            peptide.append("Trp")
        elif triple_k_mer[i] == ("CGU" or "CGC" or "CGA" or "CGG" or "AGA" or "AGG"):
            peptide.append("Arg")
        elif triple_k_mer[i] == ("AGU" or "AGC"):
            peptide.append("Ser")
        elif triple_k_mer[i] == ("GGU" or "GGC" or "GGA" or "GGG"):
            peptide.append("Gly")
        elif triple_k_mer[i] == "AUG":
            peptide.append("Met")
    all_sequence = ""
    for i in range(0, len(peptide)):
        all_sequence += peptide[i] + ""
    return all_sequence


mass_table = {}


# Homework question 4C
def generate_the_spec(peptide):
    linear_spec = []
    cyclic_spec = []
    for i in range(0, len(peptide)):
        for j in range(0, len(peptide)):
            linear_spec.append(peptide[i:j + 1])
    for i in range(2, len(peptide)):
        for j in range(0, i - 1):
            cyclic_spec.append(peptide[i:len(peptide)])
    total_mass = linear_spec + cyclic_spec
    return total_mass


def calc_spec(peptide_1):
    count = {}
    for i, j in enumerate(generate_the_spec(peptide_1)):
        count[i] = 0
        for a in j:
            count[i] = count[i] + int(mass_table[a])
    return count


# Homework question 4F
def cyc_scoring(amino_acid, spec_col):
    spec_mass = generate_the_spec(amino_acid)
    total = 0
    for i in range(0, len(spec_mass)):
        total=total+spec_mass[i]
    count = [1]+[0]*total
    for i in range(0, len(spec_col)):
        for j in spec_col:
            count[j] = count[i-j]
    return count[total]
