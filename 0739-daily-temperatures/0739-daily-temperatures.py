class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for t in range(len(temperatures)):
            while stack and temperatures[t] > temperatures[stack[-1]]:
                x = stack.pop()
                ans[x] = t - x
            stack.append(t)
        
        return ans