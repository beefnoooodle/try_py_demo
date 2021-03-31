import re


def f(s):
    while "#" in s:
        s = re.sub("(?:^|[^#])#", "", s)
    return s


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        return f(S) == f(T)
