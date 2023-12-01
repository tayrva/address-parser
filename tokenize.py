
from tokens import dir, typ, unit, states
print(dir)
def tokenize(in_seq):
    seq = []
    tok = []

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
                tokens.append('NUM')
            if j.isalpha():
                tokens.append('STR')
            if j.isalnum() is False:
                tokens.append('SEP')
            tok.append(tokens)
    return seq, tok

if __name__ == '__main__':
    import parse
    a = parse.sequence('100 Virginia Route 50')
    seq, tok = tokenize(a)
    print(seq)
    print(tok)