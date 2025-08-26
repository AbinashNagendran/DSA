class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        sw_len = len(s1)
        s1_hash = {}
        for char in s1:
            s1_hash[char] = s1_hash.get(char, 0) + 1
        
        start = 0
        end = sw_len
        while end <= len(s2):
            s = s2[start:end]
            s_hash = {}
            for char in s:
                s_hash[char] = s_hash.get(char, 0) + 1
            if s_hash == s1_hash:
                return True
            start+=1
            end+=1

        return False
        