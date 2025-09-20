class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        i = len(s) - 1
        length = 0
        while(0 <= i < len(s) and s[i] != " "):
            length+=1
            i-=1
        return length
        