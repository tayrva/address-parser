def sequence(in_str):
    char = [i for i in in_str]
    split = []
    numbers = []
    alphas = []
    separators = []
    pre = None
    seq = []
    for n in char:
        cur = None
        if n.isdigit():
            cur = 'D'
        if n.isalpha():
            cur = 'A'
        if not n.isalpha() and not n.isdigit():
            cur = 'S'
        if pre is None:
            seq.append(n)
        elif cur == pre:
            seq.append(n)
        else:
            if pre == 'D':
                numbers.append(''.join(seq))
            elif pre == 'A':
                alphas.append(''.join(seq))
            elif pre == 'S':
                separators.append(''.join(seq))
            else:
                if debug:
                    print('Unhandled character encountered')
            split.append(''.join(filter(None, seq)))
            seq = [n]
        pre = cur

    split.append(''.join(filter(None, seq)))
    if cur == 'D':
        numbers.append(''.join(seq))
    elif cur == 'A':
        alphas.append(''.join(seq))
    elif cur == 'S':
        separators.append(''.join(seq))
    else:
        if debug:
            print('Non-alphanumeric character encountered')
    #    if debug:
    #        print('Latest\nSplit: {}\nNmbrs: {}\nAlpha: {}\nSeps: {}'.format(split, numbers, alphas, separators))
    #    print('TEST',split, numbers, alphas, separators)
    return split


if __name__ == '__main__':
    print(sequence('101A Main Street'))
