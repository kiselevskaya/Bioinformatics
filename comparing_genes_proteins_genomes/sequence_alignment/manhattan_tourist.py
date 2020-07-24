

def manhattan_tourist(n, m, down, right):
    '''
    :param n: number of rows
    :param m: number of columns
    :param down: matrix for weight of vertical edges
    :param right: matrix for weight of horizontal edges
    :return: integer - the biggest weight in path from position 0,0 to n,m
    '''
    pass


if __name__ == '__main__':
    n, m = 4, 4
    down = [[1, 4, 4, 5], [0, 6, 4, 6], [2, 5, 5, 8], [4, 2, 2, 5], [3, 1, 1, 3]]
    right = [[3, 2, 4, 0], [3, 2, 4, 2], [0, 7, 3, 3], [3, 3, 0, 2], [1, 3, 2, 2]]
    print(manhattan_tourist(n, m, down, right))   # 34

    # 0-3---2---4---0-
    # |   |   |   |   |
    # 1   0   2   4   3
    # |   |   |   |   |
    # --3-+-2-+-4-+-2--
    # |   |   |   |   |
    # 4   6   5   2   1
    # |   |   |   |   |
    # --0-+-7-+-3-+-3--
    # |   |   |   |   |
    # 4   4   5   2   1
    # |   |   |   |   |
    # --3-+-3-+-0-+-2--
    # |   |   |   |   |
    # 5   6   8   5   3
    # |   |   |   |   |
    # --1---3---2---2-?
