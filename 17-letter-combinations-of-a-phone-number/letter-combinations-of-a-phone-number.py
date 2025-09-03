class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        if digits == "":
            return res
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(index, sol):
            if len(sol) == len(digits):
                res.append(sol)
                return
            letters = digitToChar[digits[index]]
            for letter in letters:
                dfs(index + 1, sol + letter)

        dfs(0, "")
        return res
        