class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for i in s:
            if i in dic.values():
                if stack and dic[stack[-1]] == i:
                    stack.pop(-1)
                else:
                    return False
            elif i in dic.keys():
                stack.append(i)
            else:
                return False
        return len(stack) == 0
