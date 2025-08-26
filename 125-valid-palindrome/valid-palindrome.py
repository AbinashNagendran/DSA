class Solution:
    def isPalindrome(self, s: str) -> bool:
        formattedString = ""
        for letter in s.lower(): 
            if letter.isalnum():
                formattedString = formattedString + letter
        left = 0
        right = len(formattedString) - 1

        return formattedString == formattedString[::-1]
        