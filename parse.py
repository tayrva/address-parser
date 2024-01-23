def sequence(in_str):
    char = [i for i in in_str]
    split = in_str.split(' ')
    numbers = []
    alphas = []
    separators = []
    others = []
    pre = None
    seq = []
    map = []
    for n in char:
        cur = None
        if n.isdigit():
            cur = 'D'
        elif n.isalpha():
            cur = 'A'
        elif n.isspace():
            cur = 'W'
        elif n in ('-', '/', '\\', '.'):
            cur = 'S'
        else:
            cur = 'O'
        if pre is None:
            seq.append(n)
        elif cur == pre:
            seq.append(n)
        else:
            if pre == 'D':
                numbers.append(''.join(seq))
            elif pre == 'A':
                alphas.append(''.join(seq))
            elif pre in ('S', 'W'):
                separators.append(''.join(seq))
            elif pre == 'O':
                others.append(''.join(seq))
            else:
                if debug:
                    print('Unhandled character encountered')
            map.append(''.join(filter(None, seq)))
            seq = [n]
        pre = cur

    map.append(''.join(filter(None, seq)))
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
    return split, alphas, numbers, separators, others, map


if __name__ == '__main__':
    for i in sequence('509 V E S Road'):
        print(i)
