# Hamming Distance Problem
def distance(pattern, dna):
    i = 0
    count = 0
    while i < len(pattern):
        if pattern[i] != dna[i]:
            count += 1
        i += 1
    return count


# For finding the all possible k-mers
def all_k_mers(dna, k):
    k_mers = []
    for i in range(0, len(dna) - 1):
        k_mers.append(dna[i:i + k])
    return k_mers


# For the find best k-mer
def frequency_map(text, k):
    freq_map = {}
    n = len(text)
    for i in (0, n - k):
        pattern = text[i:i + k]
        if not freq_map.__contains__(pattern):
            freq_map[pattern] = 1
        else:
            freq_map[pattern] = freq_map[pattern] + 1
    return freq_map


# Median String Problem (2B)
def median_string_problem(dna, k):
    best_k_mer = list(frequency_map(dna, k))
    possible_k_mers = all_k_mers(dna, k)
    for i in range(0, len(possible_k_mers)):
        if distance(possible_k_mers[i], dna) < distance(best_k_mer[0], dna):
            best_k_mer = possible_k_mers[i]

    return best_k_mer
