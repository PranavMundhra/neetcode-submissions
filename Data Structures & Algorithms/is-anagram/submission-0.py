class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        key = set(s)

        if len(s) != len(t):
            return False
        
        for i in key:
            if s.count(i) != t.count(i):
                return False
        
        return True