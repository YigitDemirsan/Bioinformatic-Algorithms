def pattern_count(pattern, text):
    count = text.count(pattern)
    return count


# Homework question 1B
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


def frequent_word(text, k):
    freq_pattern = []
    freq_map = frequency_map(text, k)
    max_count = max(freq_map.values())
    for i in freq_map:
        if freq_map[i] == max_count:
            freq_pattern.append(i)
    return freq_pattern


print("HOMEWORK QUESTION 1B")
print(frequent_word("AAAATTTGCAGCATTTAAAGCATTTGCA", 3))


# Homework question 1C
def reverse_complement(text):
    dna = []
    for i in range(0, len(text) - 1):
        dna.append(text[i])
    print("Original DNA")
    print(dna)
    for i, n in enumerate(dna):
        if n == "A" or n == "a":
            dna[i] = "T"
        elif n == "T" or n == "t":
            dna[i] = "A"
        elif n == "G" or n == "g":
            dna[i] = "C"
        else:
            dna[i] = "G"
    print("Reverse Complement of current DNA")
    return dna


print("HOMEWORK QUESTION 1C")
print(reverse_complement("ATATGCTAGCCCTAGTCCCTAGC"))


# Homework question 1D
def pattern_matching(pattern, genome):
    starting_point = []
    for i in range(0, len(genome)):
        if pattern == genome[i:i+len(pattern)]:
            starting_point.append(i)
    return starting_point


print("HOMEWORK QUESTION 1D")
print(pattern_matching("ATA", "ATAGCATTACCGATAGCCATTTATATA"))


# Homework question 1E
def remove_duplicates(target):
    a = []
    for i in range(0, len(target)):
        a.append(target[i])
    return list(set(a))


def find_clumps(genome, k, l, t):
    patterns = []
    n = len(genome)
    for i in range(0, n - l):
        window = genome[i: i + k]
        freq_map = frequency_map(window, k)
        for pattern in freq_map:
            if freq_map[pattern] >= t:
                patterns.append(pattern)
    patterns = remove_duplicates(patterns)
    return patterns


print("HOMEWORK QUESTION 1E")
print(find_clumps("ATATGCTAGCCCTAGTCCCTAGCATATGCTAGCCCTAGTCCCTAGC", 3, 2, 2))
