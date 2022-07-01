import re
REGS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def val(cnpj):
    cnpj = n(cnpj)

    try:
        if seq(cnpj):
            return False
    except:
        return False

    try:
        n_cnpj = dig(cnpj=cnpj, dig=1)
        n_cnpj = dig(cnpj=n_cnpj, dig=2)
    except Exception as e:
        return False

    if n_cnpj == cnpj:
        return True
    else:
        return False


def dig(cnpj, dig):
    if dig == 1:
        regs = REGS[1:]
        n_cnpj = cnpj[:-2]
    elif dig == 2:
        regs = REGS
        n_cnpj = cnpj
    else:
        return None

    t = 0
    for i, reg in enumerate(regs):
        t += int(cnpj[i]) * reg

    dig = 11 - (t % 11)
    dig = dig if dig <= 9 else 0

    return f'{n_cnpj}{dig}'


def seq(cnpj):
    seq = cnpj[0] * len(cnpj)

    if seq == cnpj:
        return True
    else:
        return False


def n(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)
