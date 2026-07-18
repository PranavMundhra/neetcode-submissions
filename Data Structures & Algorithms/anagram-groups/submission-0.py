class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        h = {}
        for i in strs:
            key = ''.join(sorted(i))
            if key in h:
                h[key].append(i)
            else:
                h[key] = [i]
            
        return list(h.values())