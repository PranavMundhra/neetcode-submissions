class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for i in nums:
            if i not in h:
                h[i] = 1
            else:
                h[i] += 1
        
        ans = heapq.nlargest(k, h, key= h.get)

        return ans