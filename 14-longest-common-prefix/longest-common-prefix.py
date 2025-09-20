class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        for i in range(len(strs[0])):
            letter = strs[0][i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != letter:
                    return prefix
            prefix = prefix + letter
        return prefix
                    
                

                
        