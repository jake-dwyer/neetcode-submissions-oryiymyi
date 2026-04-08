class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        ans = []
        for i in sorted(count, key=count.get, reverse=True):
            ans.append(i)   
        
        return ans[:k]
        



