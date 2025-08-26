class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket == ")" and stack:
                removed = stack.pop()
                if removed != "(":
                    return False
            elif bracket == "]" and stack:
                removed = stack.pop()
                if removed != "[":
                    return False
            elif bracket == "}" and stack:
                removed = stack.pop()
                if removed != "{":
                    return False
            else:
                stack.append(bracket)
        if stack:
            return False
        return True
        