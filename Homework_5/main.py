# Homework question 5C
def longest_com_sqn(str1, str2):
    # Hamming distance approach
    # With the dynamic programming approach
    adjacent_mat = [["" for x in range(len(str2))] for x in range(len(str1))]
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                if i == 0 or j == 0:
                    adjacent_mat[i][j] = str1[i]
                else:
                    adjacent_mat[i][j] = adjacent_mat[i - 1][j - 1] + str1[i]
            else:
                adjacent_mat[i][j] = max(adjacent_mat[i - 1][j], adjacent_mat[i][j - 1], key=len)
    reverse_of = adjacent_mat[-1][-1]
    return len(reverse_of), reverse_of


# Homework question 5E
class score_M:
    def __init__(self, gap, mismatch):
        self.gap = gap
        self.mismatch = mismatch

    def match(self):
        if self == 'A':
            return 3
        elif self == 'C' or self == 'T':
            return 2
        else:
            return 1


def global_ali(str1, str2, scr_mat):
    matrix_set = []
    for index_1 in range(len(str1) + 1):
        matrix_set[0][index_1] = scr_mat.gap * index_1
    for index_1 in range(len(str2) + 1):
        matrix_set[index_1][0] = scr_mat.gap * index_1
    for index_1 in range(len(str2) + 1):
        matrix_set.append([0] * (len(str1) + 1))
    for index_1 in range(1, len(str2) + 1):
        for index_2 in range(1, len(str1) + 1):
            matrix_set[index_1][index_2] = max(
                matrix_set[index_1][index_2 - 1] + scr_mat.gap,
                matrix_set[index_1 - 1][index_2] + scr_mat.gap,
                matrix_set[index_1 - 1][index_2 - 1] + (
                    scr_mat.match(str2[index_1 - 1])
                    if str2[index_1 - 1] == str1[index_2 - 1]
                    else
                    scr_mat.mismatch
                )
            )
    str1_align = ""
    str2_align = ""
    index_1 = len(str1)
    index_2 = len(str2)

    while index_1 > 0 or index_2 > 0:

        current_score = matrix_set[index_2][index_1]

        if index_1 > 0 and index_2 > 0 and str1[index_1 - 1] == str2[index_2 - 1]:
            str1_align = str1[index_1 - 1] + str1_align
            str2_align = str2[index_2 - 1] + str2_align
            index_1 = index_1 - 1
            index_2 = index_2 - 1

        elif index_1 > 0 and (current_score == matrix_set[index_2][index_1 - 1] + scr_mat.mismatch or current_score == matrix_set[index_2][
            index_1 - 1] + scr_mat.gap):
            str1_align = str1[index_1 - 1] + str1_align
            str2_align = "-" + str2_align
            index_1 = index_1 - 1

        else:
            str1_align = "-" + str1_align
            str2_align = str2[index_2 - 1] + str2_align
            index_2 = index_2 - 1
    return str1_align, str2_align


# Homework question 6C
def num_of_breakpoints(perm):
    adjacency = 0
    portion = [0, ] + [len(perm) + 1] + perm
    for i in range(0, len(portion) - 1):
        if portion[i] + 1 == portion[i + 1]:
            adjacency = adjacency + 1
    return len(portion) - adjacency - 1
