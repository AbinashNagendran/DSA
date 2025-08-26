class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        groups = {}
        for word in strs:
            key = tuple(sorted(word))
            if groups.get(key) == None:
                groups[key] = []
            groups[key].append(word)

        for value in groups.values():
            answer.append(value)

        return answer


            
                    
                        
                
            



            