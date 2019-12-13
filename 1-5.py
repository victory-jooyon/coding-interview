"""
하나 빼기
"""


def edit_replace(a, b):
    edited = False
    for i in range(len(a)):
        if a[i] != b[i]:
            if edited:
                return False
            else:
                edited = True
    return True


def edit_insert(a, b):
    edited = False
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] != b[j]:
            if edited:
                return False
            else:
                edited = True
                j += 1
        else:
            i += 1
            j += 1

    return True


def edit_delete(a, b):
    pass


def minus_one(a, b):
    if len(a) == len(b):
        return edit_replace(a, b)
    elif len(a) == len(b) + 1:
        return edit_insert(b, a)
    elif len(a) + 1 == len(b):
        return edit_insert(a, b)
    else:
        return False


print(minus_one('pale', 'ple'))
print(minus_one('pales', 'pale'))
print(minus_one('pale', 'bale'))
print(minus_one('pale', 'bake'))
