class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bang = set(nums)

        if len(bang) != len(nums):
            return True
        
        return False