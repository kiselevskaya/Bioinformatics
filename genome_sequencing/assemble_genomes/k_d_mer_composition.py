

def k_d_mer_composition(text, k, d):
    composition = {}
    for i in range(len(text)-(2*k+d)+1):
        if text[i:i+k] not in composition.keys():
            composition[text[i:i+k]] = [text[i+k+d:i+2*k+d]]
        else:
            composition[text[i:i+k]].append(text[i+k+d:i+2*k+d])
    return dict(sorted(composition.items()))


if __name__ == '__main__':
    output = ''
    composition = k_d_mer_composition('TAATGCCATGGGATGTT', 3, 2)
    for key, value in composition.items():
        if len(value) == 1:
            output += '({}|{})'.format(key, value[0])
        else:
            for pair in value:
                output += '({}|{})'.format(key, pair)
    print(output)
