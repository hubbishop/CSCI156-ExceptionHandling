__author__ = 'Dark-Knight'

ssn = 'please enter your social security in the format ###-##-####:'


def social(r):
    try:
        aaa, gg, ssss = input(r).split('-')
    except ValueError:
        print('you must input a dash')
        return None
    if aaa == '078'and gg == '05' and ssss == '1120':
        return None
    if len(aaa) != 3:
        return None
    if len(gg) != 2:
        return None
    if len(ssss) != 4:
        return None
    try:
        aaa = int(aaa)
        gg = int(gg)
        ssss = int(ssss)
    except ValueError:
        print('you must input a valid social security number')
        return None
    if str(aaa) == '000':
        return None
    elif 900 <= int(aaa) <= 999:
        return None
    elif int(aaa) == 666:
        return None
    if str(gg) == '00':
            return None

    elif str(ssss) == '0000':
        return None
    else:
        return aaa, gg, ssss


def usersocial(r):
    while True:
        x = social(r)
        if x is not None:
            return x

print(usersocial(ssn))