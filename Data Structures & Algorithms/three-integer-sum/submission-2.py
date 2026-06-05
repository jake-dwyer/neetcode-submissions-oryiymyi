class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []

        sortedNums = sorted(nums)
        print("sorted nums: ", sortedNums)

        i = 0
        k = len(sortedNums) - 1

        for i in range(len(sortedNums) - 2):
            j = i+1
            k = len(sortedNums) - 1

            if i > 0 and sortedNums[i] == sortedNums[i-1]:
                continue

            while j < k:
                summed = sortedNums[i] + sortedNums[j] + sortedNums[k]
                if summed > 0:
                    k -= 1
                elif summed < 0:
                    j += 1
                else:
                    print("hit else, found triplet ", [sortedNums[i], sortedNums[j], sortedNums[k]])
                    ans.append([sortedNums[i], sortedNums[j], sortedNums[k]])
                    j += 1
                    while j < k and sortedNums[j] == sortedNums[j - 1]:
                        j += 1

        return ans