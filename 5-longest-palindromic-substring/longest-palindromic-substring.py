class Solution(object):
    def longestPalindrome(self, s):
        longest = 0
        substring = ""
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s)):
            l, r = i, i
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                if r - l + 1 > longest:
                    substring = s[l: r + 1]
                    longest = r - l + 1
                l-=1
                r+=1

            l, r = i, i + 1
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                if r - l + 1 > longest:
                    substring = s[l: r  + 1]
                    longest = r - l + 1
                l-=1
                r+=1
        return substring


        