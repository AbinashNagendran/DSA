class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(openBracket,closeBracket,parentheses):
            if openBracket + closeBracket == n*2 and openBracket == closeBracket:
                res.append(parentheses)
                return
            if openBracket < n:
                dfs(openBracket + 1, closeBracket, parentheses + "(")
            if openBracket > closeBracket:
                dfs(openBracket, closeBracket + 1, parentheses + ")")
        dfs(0,0,"")
        return res