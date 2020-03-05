

def pattern_to_number(pattern):
    order = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    number = 0
    n = len(pattern)
    for i in range(len(pattern)):
        number += order[pattern[i]]*4**(n-1-i)
    return number


def number_to_pattern(number, k):
    order = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    pattern = ''
    dividend = number
    for i in range(k):
        pattern = list(order.keys())[list(order.values()).index(dividend % 4)] + pattern
        dividend = dividend // 4
    return pattern


def pattern_to_number_recursion(pattern):
    order = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    number = 0
    if len(pattern) == 0:
        return number
    symbol = pattern[-1]
    prefix = pattern[:-1]
    return 4 * pattern_to_number_recursion(prefix) + order[symbol]
