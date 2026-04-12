class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += str(len(i)) + "#" + i
        
        return s

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            delim = s.find("#", i)
            length = int(s[i:delim])
            i = delim + 1
            ans.append(s[i : i + length])
            i += length

        return ans