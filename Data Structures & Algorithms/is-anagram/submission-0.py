class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #  Output: Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
        sHash = Counter(s)
        tHash = Counter(t)

        if sHash == tHash:
            return True
        return False