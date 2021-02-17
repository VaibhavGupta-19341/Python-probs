def get_every_third(S):

    str3 = S.strip()
    return str3[::3]

def get_every_kth(S,k,i):

    strk = S.strip()
    return strk[i::k]

def decode_string(S):

    strd = S.strip()
    R = strd[::-1]

    f1 = strd.find('(')
    l1 = strd.find(')')
    f2 = R.find('(')
    l2 = R.find(')')

    s = strd[f1 + 1 : l1]
    r1 = R[l2 + 1 : f2]
    r = r1[::-1]
    return ( ( s.isalpha() or s.isnumeric() ) and ( r.isalpha() or r.isnumeric() ) )
