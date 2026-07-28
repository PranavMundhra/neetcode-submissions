class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            m = (l+r)//2
            total_hours = 0
            for p in piles:
                total_hours += math.ceil(float(p)/m)
            
            if total_hours <= h:
                res = m
                r = m-1
            else:
                l = m+1
        
        return res