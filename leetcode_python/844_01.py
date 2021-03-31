from typing import List
import re


def fun(s: List[str]) -> List[str]:
    while "#" in s:
        s = re.sub("(?:^|[^#])#", "", s)
    return s


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return fun(S) == fun(T)
