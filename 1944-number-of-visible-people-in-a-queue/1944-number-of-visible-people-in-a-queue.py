class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = [0] * len(heights)
        H = len(heights)
        stack = []
        for i in range(H -1, -1, -1):
            height = heights[i]
            seen = 0
            while stack and height > stack[-1]:
                stack.pop()
                seen += 1
            
            if stack:
                seen += 1
            
            res[i] = seen
            stack.append(height)
        
        return res



        