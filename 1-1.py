"""
중복이 없는가
"""


def check(string):
    assert type(string) is str
    l = []
    for i in string:
        l.append(i)

    if len(l) != len(set(l)):
        return True
    else:
        return False


# 자료구조를 추가로 사용하지 않는 알고리즘
def check_without(string):
    assert type(string) is str
    flag = ''
    string = sorted(string)
    for i in string:
        if flag == i:
            return True
        else:
            flag = i
    return False
