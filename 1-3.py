"""
URL화
"""


def change_url(string):
    assert type(string) is str
    return string.replace(' ', '%20')
