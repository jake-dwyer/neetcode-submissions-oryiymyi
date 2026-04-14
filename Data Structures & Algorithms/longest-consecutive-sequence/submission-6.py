class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        counts = []
        set_nums = set(nums)

        if len(nums) == 0:
            return 0

        if len(set_nums) == 1:
            return 1

        for i in sorted(set_nums):
            if i - 1 not in set_nums:
#               print("counts: ", counts)
                start = i
                count = 1
#               print(sorted(set_nums))
#               print("start: ", start)

            if i + 1 in set_nums:
                count += 1
#               print("count: ", count)
            counts.append(count)

        return max(counts)
