class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # default value is a list ...
        # key = count, value = list of anograms

        for s in strs:
            count = [0] * 26 # 1 for each char a-z

            # go through each char and count
            for c in s:
                # a - a = 0, z - a = 25
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s) # lists cannot be keys

        return list(res.values())
                