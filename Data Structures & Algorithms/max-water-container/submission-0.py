class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1

        m = 0
        v = 0
        while l < r:

            if heights[l] > heights[r]:
                v = heights[r]*abs(l-r)
                m = max(m,v)
                r -= 1
            else:
                
                v = heights[l]*abs(l-r)
                m = max(m,v)
                l += 1
        
        return m
