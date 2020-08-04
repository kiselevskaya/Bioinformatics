

def longest_common_subsequence_backtrack(v, w):
    '''
    :param v: characters sequence of type string
    :param w: characters sequence of type string
    :return: matrix of backtracking pointers, which take one of the three values ↓ , →, or ↘
    '''
    len_v = len(v)
    len_w = len(w)
    weight_matrix = [[0]*(len_v+1) for i in range(len_w+1)]
    backtrack = [['']*(len_v+1) for i in range(len_w+1)]

    for i in range(1, len(v)):
        for j in range(1, len(w)):
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


if __name__ == '__main__':
    print(longest_common_subsequence_backtrack.__doc__, '\n')
    lcs_backtrack = longest_common_subsequence_backtrack('ATCGTCC', 'ATGTTATA')
    for i in range(len(lcs_backtrack)):
        print(lcs_backtrack[i])
