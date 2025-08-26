class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use sliding window
        start = 0
        end = 0
        substring = set()
        output = 0

        while end < len(s):
            while s[end] in substring:
                substring.remove(s[start])
                start +=1
            substring.add(s[end])
            output = max(len(substring), output)
            end+=1
        return output






        


        
        