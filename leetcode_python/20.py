class Solution(object):
    def isValid(self, s: str) -> bool:
        dic = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for i in s:
            if i in dic.keys():
                stack.append(i)
            elif stack:
                if i == dic[stack[-1]]:
                    stack.pop(-1)
                else:
                    return False
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False
