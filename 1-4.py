"""
회문 순열
"""


def check(string):
    assert type(string) is str
    info = {}

    string = string.replace(' ', '')
    string = string.lower()

    for i in string:
        info[i] = info.get(i, 0) + 1
    info_values = info.values()

    if len(string) % 2:
        odd = False
        for value in info_values:
            if value % 2:
                if odd:
                    return False
                else:
                    odd = True

    else:
        for value in info_values:
            if value % 2 != 0:
                return False

    return True
