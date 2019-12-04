"""
순열 확인
"""


def check(a, b):
    assert type(a) is str and type(b) is str
    if sorted(a) == sorted(b):
        return True
    return False
