class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s={}
        for char in s:
            dict_s[char] = dict_s.get(char, 0) + 1

        for char in t:
            if char not in dict_s:
                return False
            dict_s[char] = dict_s[char] - 1
            if dict_s[char] < 0:
                return False
        return True
            
            
            


        
        