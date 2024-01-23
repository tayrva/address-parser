
from tokens import dir, typ, unit, states
from itertools import product

def tokenize(in_seq):
    seq = []
    tok = []

    #identify hyphens, decimals, and fractions
    sep_idx = []
    for i in in_seq:
        if 'counter' not in locals():
            counter = 0
        j = i.strip().upper()
        if j in ('-', '.', '/'):
            sep_idx.append(counter)
        counter += 1
    if sep_idx:
        counter = 0
        for idx in sep_idx:
            idx -= counter
            sep = in_seq[idx].strip()
            if idx-1 >= 0:
                pre = in_seq[idx-1]
                counter += 1
            else:
                pre = None
            if idx+1 < len(in_seq):
                post = in_seq[idx+1]
                counter += 1
            else:
                post = None
            if pre.isalpha() and post.isalpha():
                pass
            else:
                in_seq[idx] = ''.join(filter(None, [pre, sep, post]))
                if pre:
                    in_seq.pop(idx+1)
                if post:
                    in_seq.pop(idx-1)
    counter = 0
    for i in in_seq:
        tokens = []
        j = i.strip().upper()
        if j in ('', ','):
            pass
        else:
            seq.append(i.strip())
            if j in states:
                tokens.append('ST')
            if j in dir:
                tokens.append('DIR')
            if j in typ:
                tokens.append('TYP')
            if j in unit:
                tokens.append('UNIT')
            if j.isdigit():
                tokens.append('HN')
                tokens.append('NUM')
                if counter-1 > 0:
                    if 'UNIT' in tok[counter-1]:
                        tokens.append('WS')
            elif j.isalpha():
                if counter - 1 > 0:
                    if 'UNIT' in tok[counter-1]:
                        tokens.append('WS')
                    elif 'NUM' in tok[counter-1] and j in ('ST', 'ND', 'RD', 'TH'):
                        tokens.append('CARD')
                    if len(j) == 1:
                        tokens.append('CHAR')
                    else:
                        tokens.append('STR')
                elif len(j) == 1:
                    tokens.append('CHAR')
                else:
                    tokens.append('STR')
            elif j.isalnum():
                tokens.append('ALNUM')
            else:
                if '-' in j:
                    tokens.append('HYP')
                elif '/' in j:
                    split = [i.isalpha() for i in j.split('/')]
                    if False in split:
                        tokens.append('STR')
                    else:
                        tokens.append('HN')
                        tokens.append('FRAC')
                elif '.' in j:
                    split = [i.isalpha() for i in j.split('.')]
                    if False in split:
                        try:
                            float(i)
                            tokens.append('HN')
                            tokens.append('DEC')
                        except:
                            tokens.append('STR')
                    else:
                        tokens.append('HN')
                        tokens.append('DEC')

                else:
                    tokens.append('SEP')
            tok.append(tokens)
            counter += 1
    iter = list(product(*tok))

    return seq, tok, iter

if __name__ == '__main__':
    import parse
    a = parse.sequence('1120 North 27th Street')[-1]
    print(1, a)
    seq, tok, iter = tokenize(a)
    print(2, seq)
    print(3, tok)
    print(4)
    for i in iter:
        print(i)

