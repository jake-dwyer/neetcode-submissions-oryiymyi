class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = nums.count(0)

        if zero_count > 1:
            return [0] * len(nums)

        for i in nums:
            if i != 0:
                product = product * i
        
        ans = [0] * len(nums)

        for i in range(len(ans)):
            if zero_count == 1:
                if nums[i] == 0:
                    ans[i] = product
                else:
                    ans[i] = 0
            else:
                ans[i] = int(product / nums[i])
        
        return ans