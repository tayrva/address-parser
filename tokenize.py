
from tokens import dir, typ, unit, states
from itertools import product
print(dir)
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
        if j in ('', '.', ','):
            pass
        else:
            seq.append(i)
            if j in states:
                tokens.append('ST')
            if j in dir:
                tokens.append('DIR')
            if j in typ:
                tokens.append('TYP')
            if j in unit:
                tokens.append('UNIT')
            if j.isnumeric():
                tokens.append('HN')
                if counter-1 > 0:
                    if 'UNIT' in tok[counter-1]:
                        tokens.append('WS')
                else:
                    tokens.append('NUM')
            if j.isalpha():
                if counter - 1 > 0:
                    if 'UNIT' in tok[counter-1]:
                        tokens.append('WS')
                    elif len(j) == 1:
                        tokens.append('CHAR')
                    else:
                        tokens.append('STR')
                elif len(j) == 1:
                    tokens.append('CHAR')
                else:
                    tokens.append('STR')
            if j.isalnum() is False:
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
    a = parse.sequence('101 1 North Avenue A APT A')
    print(a)
    seq, tok, iter = tokenize(a)
    print(seq)
    print(tok)
    for i in iter:
        print(i)

