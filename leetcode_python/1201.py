class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        result = ""
        index = 0

        for i in range(len(S)):
            if S[i] == "(":
                stack.append("(")
            else:
                stack.pop()
                if len(stack) == 0:
                    result += S[index + 1 : i]
                    index = i + 1
        return result
