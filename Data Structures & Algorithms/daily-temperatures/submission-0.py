class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # temp, index

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # top of stack & temp
                temp, sIndex = stack.pop()
                res[sIndex] = (i - sIndex)
            stack.append([t, i])
        return res

        