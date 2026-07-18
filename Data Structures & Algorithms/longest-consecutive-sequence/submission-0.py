class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = set(nums)
        l = 0
        for i in h:
            if i-1 not in h:
                curr = 1
                while i+curr in h:
                    curr += 1
                l = max(l,curr)
        
        return l