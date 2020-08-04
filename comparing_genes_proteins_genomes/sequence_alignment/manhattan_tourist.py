

def manhattan_tourist(n, m, down, right, cross=None):
    '''
    :param n: number of rows
    :param m: number of columns
    :param down: matrix for weight of vertical edges
    :param right: matrix for weight of horizontal edges
    :return: integer - the biggest weight in path from position 0,0 to n,m
    '''

    weight_matrix = []
    for i in range(n+1):
        weight_matrix.append([0]*(m+1))

    for i in range(1, n+1):
        weight_matrix[i][0] = weight_matrix[i-1][0] + down[i-1][0]
    for j in range(1, m+1):
        weight_matrix[0][j] = weight_matrix[0][j-1] + right[0][j-1]

    for i in range(1, n+1):
        for j in range(1, m+1):
            try:
                weight_matrix[i][j] = max(weight_matrix[i-1][j] + down[i-1][j], weight_matrix[i][j-1] + right[i][j-1], weight_matrix[i-1][j-1] + cross[i][j])
            except Exception as e:
                weight_matrix[i][j] = max(weight_matrix[i-1][j] + down[i-1][j], weight_matrix[i][j-1] + right[i][j-1])
    return weight_matrix[n][m]


if __name__ == '__main__':
    import os

    data_dir = os.path.abspath('..\\sequence_alignment\\text_files')
    dataset = open(data_dir+'\\LongestPathGrid\\dataset_261_10.txt', 'r')
    input = [string.strip('\n') for string in dataset.readlines()]
    dataset.close()

    n, m = int(input[0].split()[0]), int(input[0].split()[1])
    down = [[int(e) for e in E.split()] for E in input[1:input.index('-')]]
    right = [[int(e) for e in E.split()] for E in input[input.index('-')+1:]]
    print(manhattan_tourist.__doc__)
    print(manhattan_tourist(n, m, down, right))   # 88
