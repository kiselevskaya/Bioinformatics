

def longest_common_subsequence_backtrack(v, w):
    '''
    :param v: characters sequence of type string
    :param w: characters sequence of type string
    :return: matrix of backtracking pointers, which take one of the three values ↓ , →, or ↘
    '''

    max_len = max(len(v), len(w))
    weight_matrix = [[0]*(max_len+1) for i in range(max_len+1)]
    backtrack = [['']*(max_len+1) for i in range(max_len+1)]

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            match = 0
            if v[i-1] == w[j-1]:
                match = 1
            weight_matrix[i][j] = max(weight_matrix[i-1][j], weight_matrix[i][j-1], weight_matrix[i-1][j-1] + match)
            if weight_matrix[i][j] == weight_matrix[i-1][j]:
                backtrack[i][j] = '↓'
            elif weight_matrix[i][j] == weight_matrix[i][j-1]:
                backtrack[i][j] = '→'
            elif weight_matrix[i][j] == weight_matrix[i-1][j-1]+match:
                backtrack[i][j] = '↘'

    return backtrack


def output_lcs(backtrack, v, i, j):
    '''
    :param backtrack: matrix of backtracking pointers, which take one of the three values ↓ , →, or ↘
    :param v: string
    :param i: length of string v
    :param j: length of string w
    :return: longest common subsequence of strings v and w
    '''
    # 1. recursive approach
    # if i == 0 or j == 0:
    #     return ''
    # if backtrack[i][j] == '↓':
    #     return output_lcs(backtrack, v, i-1, j)
    # elif backtrack[i][j] == '→':
    #     return output_lcs(backtrack, v, i, j-1)
    # else:
    #     return output_lcs(backtrack, v, i-1, j-1) + v[i]

    # 2. iterative approach (more efficient)
    lcs = []
    while i > 0 and j > 0:
        if backtrack[i][j] == "↘":
            lcs.append(v[i-1])
            i -= 1
            j -= 1
        elif backtrack[i][j] == "↓":
            i -= 1
        else:
            j -= 1
    return ''.join(lcs[::-1])


if __name__ == '__main__':
    import os
    data_dir = os.path.abspath('..\\sequence_alignment\\text_files')
    dataset = open(data_dir+'\\LongestCommonSubsequence\\inputs\\dataset_245_5.txt', 'r')
    input = [string.strip('\n') for string in dataset.readlines()]
    dataset.close()

    v, w = input[0], input[1]
    i, j = len(v), len(w)
    backtrack = longest_common_subsequence_backtrack(v, w)
    # for i in range(len(backtrack)):
    #     print(backtrack[i])

    print(output_lcs(backtrack, v, i, j))
